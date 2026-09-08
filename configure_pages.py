#!/usr/bin/env python3
"""Personalize this local Beacon package. Does not publish or verify compliance."""
from __future__ import annotations
import argparse
from html import escape
from pathlib import Path
import re
import sys

FILES = ('privacy.html', 'terms.html', 'eula.html', 'index.html',
         'privacy.txt', 'terms.txt', 'CAMPAIGN_COPY.txt')
PLACEHOLDER = '[LEGAL OPERATOR NAME]'
DEFAULT_EMAIL = 'idealimagellc@gmail.com'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--operator', help='Actual legal operator registered with Twilio')
    parser.add_argument('--email', help='Monitored support/privacy address')
    parser.add_argument('--reviewed', action='store_true',
                        help='Acknowledge content review and remove visible draft notices')
    args = parser.parse_args()
    if not (args.operator or args.email or args.reviewed):
        parser.error('Provide --operator, --email, and/or --reviewed.')
    if args.operator and (not args.operator.strip() or '[' in args.operator or ']' in args.operator
                          or len(args.operator) > 250 or '\n' in args.operator):
        parser.error('Enter an actual operator name without placeholder brackets or newlines.')
    if args.email and not re.fullmatch(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", args.email):
        parser.error('Provide a valid support email address.')
    root = Path(__file__).resolve().parent
    changes: dict[Path, str] = {}
    for filename in FILES:
        path = root / filename
        if not path.is_file():
            print(f'Missing expected file: {path}', file=sys.stderr)
            return 1
        text = path.read_text(encoding='utf-8')
        if args.operator:
            value = escape(args.operator.strip(), quote=True) if path.suffix == '.html' else args.operator.strip()
            if path.suffix == '.html':
                text = text.replace('<mark class="required-detail">'+PLACEHOLDER+'</mark>', value)
            text = text.replace(PLACEHOLDER, value)
        if args.email:
            value = escape(args.email, quote=True) if path.suffix == '.html' else args.email
            text = text.replace(DEFAULT_EMAIL, value)
        if args.reviewed:
            if PLACEHOLDER in text:
                print('Refusing to remove draft notice: legal operator is still unspecified.', file=sys.stderr)
                return 1
            if path.suffix == '.html':
                text = re.sub(r'<!-- DRAFT_NOTICE_START -->.*?<!-- DRAFT_NOTICE_END -->\n?', '', text, flags=re.S)
        changes[path] = text
    # Validate everything before writing; atomic replacement per file.
    for path, text in changes.items():
        temp = path.with_name(path.name + '.tmp')
        temp.write_text(text, encoding='utf-8')
        temp.replace(path)
    print('Updated local files. No deployment or Twilio changes were made.')
    if args.reviewed:
        print('Draft banners removed based on your acknowledgment, not an automated compliance review.')
    else:
        print('Review banners remain. Verify practices before using --reviewed.')
    print('Complete actual URL placeholders in CAMPAIGN_COPY.txt and follow START_HERE.md.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
