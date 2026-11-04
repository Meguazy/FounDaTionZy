# Validation evidence

- Scope / related requirement / step criterion: unset
- Source revision or tree / relevant configuration: unset
- Date / environment / tool versions: unset
- Boundary: structural / unit / contract-fake / real integration /
  application-E2E-with-declared-dependencies / isolated-live acceptance
- Actual dependencies and fixture scope: unset
- Authorization reference where required: unset
- Earlier record corrected or replaced, if any: unset

| Command or procedure actually run | Outcome / counts | Sanitized evidence | Limits |
| --- | --- | --- | --- |

## Interpretation

State exactly which claim the evidence supports. Record failures, skips, and
not-run gates separately. Do not turn an exit code or an agent assertion into
proof of behavior it did not check.

## Invalidation and follow-up

Describe which changes require rerunning this evidence and what remains open.
Link the owner acceptance separately if given.

Keep this result tied to its checked inputs. A new run or substantive correction
gets a separate linked record, preserving the original result and its limits.
The owning step or contract records which evidence currently supports its claims;
an old pass does not renew itself when relevant inputs or external conditions change.
