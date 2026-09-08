# Beacon policy and messaging-page package

Prepared September 8, 2026. These are editable, implementation-dependent drafts,
not a legal opinion or a promise of carrier/Twilio approval. No files have been
published to GitHub, and no Twilio campaign or backend has been configured.

## What is included

- `privacy.html`: the public Privacy Policy, including SMS, AI, and integrations.
- `terms.html`: the public Terms & Conditions, including program-specific SMS terms.
- `eula.html`: an identical full-content copy of the Terms for existing site links.
  Keep this synchronized with `terms.html`; do not leave the old conflicting EULA.
- `index.html`: replacement overview text so the homepage no longer describes
  all of Beacon as a tool with no other people or communications providers.
- `privacy.txt` and `terms.txt`: editable, readable text copies of the main content.
- `CAMPAIGN_COPY.txt`: proposed web-chat consent flow, consent disclosure, and
  confirmation / HELP / STOP / representative message copy.
- `configure_pages.py`: optional local helper for safely replacing the legal
  operator name and email across the package and removing the review banner
  after an explicit review acknowledgment. It does not deploy anything.

Each HTML page contains its own CSS. There are no external fonts, libraries,
tracking pixels, scripts, or asset dependencies. Existing connect.html,
disconnect.html, and backend code are not overwritten by this package.
The package does not include a working chatbot, signup form, SMS webhook,
database, or consent-evidence screenshots.

## Required before publication

1. Replace `[LEGAL OPERATOR NAME]` with the exact operator behind the registered
   Twilio brand. Use the trust's legal name only when that trust is actually the
   registered/operator entity. Do not invent a company or describe Aaron Jones
   as a trustee without verifying that role. The drafts identify him only as the
   administrative contact. A trust's entity classification or registration issue
   may need Twilio support or counsel; changing page wording will not fix a
   mismatched registration. Do not publish an EIN or private trust documents.

2. Confirm the public support email `idealimagellc@gmail.com`. It came from the
   existing Beacon privacy page. Use a monitored address with authority to handle
   support, opt-out, and privacy requests. Update Aaron Jones's contact name if
   the operator designates a different person.

3. Verify the service assumptions. These drafts describe a private, adult-oriented,
   non-promotional trust-administration assistant: conversational replies,
   scheduling, requested reminders, and administrative updates. They do not cover
   cold outreach, marketing, fundraising, securities promotion, lending, debt
   collection, or a public multi-tenant service. Broader real use needs accurate
   descriptions, consent, and campaign review; do not conceal it with these words.
   The SMS path is individual consent, not one person consenting for a group.
   If the assistant joins group conversations, document each person's consent,
   disclose who can see messages and phone numbers, and revise these pages before
   launch to accurately cover that visibility.

4. Verify data practices with the developer. The no-sale, no-marketing-sharing,
   no-transfer-of-consent, no-general-purpose-model-training, restricted-access,
   deletion, and opt-out statements are commitments to implement, not an audit of
   your current systems. Check Twilio, AI API contracts and account settings,
   hosting, logs, backups, internal tools, recipients, retention schedules, and
   staff access. Do not publish a no-training promise while using a provider or
   configuration that allows training on this content. Add actual provider names
   where useful or legally required; update disclosures for analytics or other
   processing that is not covered. Do not state that all information stays on
   local hardware when a cloud messaging or AI provider processes it.

5. Keep the QuickBooks paragraphs only if Beacon still supports the authorized
   accounting connection described on the original site. Confirm scopes and
   disconnection behavior. These pages do not constitute a separate Intuit API
   compliance review. Public messaging enrollment must not grant accounting or
   beneficiary-record access. Review existing connect/disconnect pages and
   repository metadata for outdated all-app claims.

6. Implement and test consent before using the proposed campaign copy. Place all
   material SMS disclosures next to the affirmative control, not only in these
   linked legal pages. Store consent evidence securely. Test STOP, HELP, clear
   natural-language withdrawals, manual email opt-outs, queued sends, and
   re-enrollment. Do not rely on the AI to decide whether STOP should be obeyed.
   These HTML documents do not create that functionality.

7. Have appropriate counsel review the legal operator, trust-specific wording,
   privacy rights, actual jurisdictions, retention obligations, and service
   limitations. The broad retention language is not a substitute for adopting
   and following an internal retention schedule.

8. Set the update date to the date you adopt the final pages. Remove the marked
   draft-notice block only after completing review. Search all files for `[` and
   `]` and resolve the deployment placeholders (message-template variables are
   intentional). Never submit pages containing `[LEGAL OPERATOR NAME]`.

## Optional local configuration helper

Requires Python 3.10 or newer. Start with a backup or a copy of this package.
From inside this folder run, using the REAL legal operator and contact:

    python configure_pages.py --operator 'Your actual legal operator name' --email 'your-monitored-email@example.com'

This fills in the name/email but intentionally keeps the visible review banner.
After verifying the contents and practices, remove the banner with:

    python configure_pages.py --reviewed

`--reviewed` is your acknowledgment, not automated validation or legal approval.
The helper refuses banner removal while the legal-operator placeholder remains.
The message-flow URL placeholders in CAMPAIGN_COPY.txt must still be replaced
with actual live enrollment, policy, terms, and evidence URLs.

## Publish to the existing Beacon repository

Back up the current pages before overwriting them. Put the four HTML files into
the directory actually published by GitHub Pages (commonly main / root). Do not
upload the ZIP itself and expect it to become a website. Retain the existing
application/integration files. Either adopt the new index.html or revise the
old homepage to say the same thing about recipients and provider processing.
The original homepage, policy, EULA, and repository description all used broad
single-user/no-sharing wording; leaving contradictions may cause review issues.

For a branch deployment, go to the Beacon repository's Settings > Pages,
choose Deploy from a branch, select main and /(root) if those are your intended
publishing sources, then save. Use the actual URL displayed by GitHub Pages.
Do not change an already working GitHub Actions or custom-domain deployment
without checking the existing configuration.

With the usual project-site configuration and no custom domain, the expected
addresses would be:

    https://amj9r3.github.io/Beacon/
    https://amj9r3.github.io/Beacon/privacy.html
    https://amj9r3.github.io/Beacon/terms.html

These are EXPECTED POST-DEPLOYMENT addresses, not a claim that they are live.
The authoring session could read the public GitHub source but could not verify
a functioning Pages deployment. Prefer the real rendered website address over
a github.com/.../blob/... source-code view. Use the same website domain for the
campaign, privacy, and terms. Open the finished URLs in a logged-out/private
browser, test their internal links, and confirm that no login is needed.

In the Twilio registration form, use the actual public privacy and terms URLs
in their respective fields. In message_flow include the REAL enrollment URL
and a publicly accessible URL showing the implemented opt-in experience. Do
not claim the informational homepage is a working signup form. Publish only
redacted screenshots of the real flow, using test data and no private numbers,
trust documents, or financial information. Screenshots of these policy pages
alone are not proof of the consent mechanism.

## Implementation notes for the proposed flow

The principal draft is WEB-CHAT consent before the first outbound SMS. Do not
send an unsolicited SMS merely asking whether a person agrees to receive SMS.
If the person texts the agent first, respond to that inquiry, but obtain separate
permission before recurring notifications. In a group, one participant's yes
cannot substitute for everyone else's consent.

If you use text-to-join, paper consent, or another route instead, replace the
proposed web-chat flow with what actually occurs and document every active
route. Generic language such as "the AI asks them if it is okay to chat" does
not specify sender, channel, scope, disclosures, affirmative choice, or proof.

For a low-volume private assistant, choose the campaign type that matches its
actual traffic and the choices available to the registered brand. Do not select
a category merely because it seems easier to approve. The copy does not decide
your legal entity type, eligibility, or campaign classification.

## Source notes

Requirements were checked against the following official materials on
September 8, 2026. These are source references for the drafting notes, not a
claim that the published pages have been approved by Twilio or a regulator.

- Twilio Messaging Policy: prior, specific consent; limited inbound-conversation
  permission; consent records; sender identification; opt-out behavior.
  https://www.twilio.com/en-us/legal/messaging-policy
- Twilio privacy-policy rejection guidance (30908): mobile information and
  consent protections; avoiding conflicting policies.
  https://www.twilio.com/docs/api/errors/30908
- Twilio consent-flow rejection guidance (30909 and 30924): complete workflow,
  public evidence, and disclosures beside the consent control.
  https://www.twilio.com/docs/api/errors/30909
  https://www.twilio.com/docs/api/errors/30924
- Twilio business/campaign information: public policy and terms URLs, field
  lengths, program sample messages, and relationship to the registered brand.
  https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/collect-business-info
- Twilio Terms URL requirement (30934).
  https://www.twilio.com/docs/api/errors/30934
- Twilio Advanced Opt-Out: keyword behavior and OptOutType webhooks.
  https://www.twilio.com/docs/messaging/tutorials/advanced-opt-out
- GitHub Pages publishing instructions.
  https://docs.github.com/en/pages/quickstart
- Existing Beacon policy used for the public name, contact, and original scope.
  https://github.com/amj9r3/Beacon/blob/main/privacy.html
