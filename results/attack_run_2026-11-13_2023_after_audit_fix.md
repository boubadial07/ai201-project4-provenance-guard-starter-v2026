# Attack run â€” after_audit_fix

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks Â· 2026-11-13 20:23
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds â€” read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table â€” either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `02533e55-9085-44f8-b8fa-41ce7a9d85ad` | human | 0.271 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f7b62fa2-f596-44f8-9fe3-55a518cc6ff5` | unsure | 0.392 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9f4fe297-ac15-4597-8ecd-59c07db41042` | unsure | 0.496 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `32e1c9e2-869b-4c7a-8af8-e2e30d3b586b` | unsure | 0.495 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `fa8d6823-c87d-4c11-a239-97c558d49003` | human | 0.304 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `57d34db1-0a8a-48e5-8bf9-d58c1b656a01` | human | 0.349 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `5cfec238-4b7e-4989-9bcd-b11361a5dc68` | unsure | 0.549 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `d82ec795-3b6c-4426-bcd4-ab22d9347533` | human | 0.293 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `a403fcd6-4a99-416f-8bf6-a87f113b0a3c` | unsure | 0.506 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `541549b8-934b-4854-81c7-e1de7304b876` | ai | 0.713 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `21b99219-0ede-4d34-b344-4f58768c2712` | unsure | 0.480 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `43bc36d9-42b9-4408-949e-f0868ebe49f7` | unsure | 0.572 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `34c12ace-c17f-4b92-9b84-75b4bb11c915` | unsure | 0.589 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `ed6fcbdf-3582-4905-8749-a9a87f4b7604` | unsure | 0.588 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `cd20b1ba-9ac2-41ce-bba7-926599556b53` | unsure | 0.628 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `1d8c092a-3b8e-4425-9755-b0495f458ba8` | unsure | 0.598 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `9e4671de-7338-4adc-ac2c-ccaabc085ffc` | unsure | 0.621 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `0448226c-fa03-46dc-9ac9-a709504f96b7` | unsure | 0.394 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1a5a3d82-8208-41b6-bd38-22174a1437d2` | human | 0.325 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `842c8335-50d5-43dd-89dc-e7b76e1bba79` | human | 0.209 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f1d557fb-39a5-47b8-b356-e3382b2d0489` | unsure | 0.453 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `2874ed6e-106b-48dd-bfd8-1542d9dda143` | unsure | 0.428 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `2d5d74e6-0f09-4e49-bbc1-6a6ab16fbffd` | unsure | 0.562 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c2fd8869-ec49-4c15-b9c7-e8545d0d1d84` | unsure | 0.451 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `â€”` | â€” | â€” | HELD |
| MF02 | malformed | text is a single character | 400 | `â€”` | â€” | â€” | HELD |
| MF03 | malformed | text is control characters | 200 | `5a83d882-8f73-4b7a-b62c-3ec70ce7ea88` | human | 0.325 | HELD |
| MF04 | malformed | text is only punctuation | 400 | `â€”` | â€” | â€” | HELD |
| MF05 | malformed | text is a very long single word | 200 | `fa1491de-cfae-4ded-9b6e-36f3996a159f` | ai | 0.665 | HELD |
| MF06 | malformed | text is emoji only | 400 | `â€”` | â€” | â€” | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `301d1cd2-572a-4c69-b651-6ebfe735f4f1` | ai | 0.802 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `b30ada21-87ad-4f50-a064-82a8189f0013` | ai | 0.787 | HELD |
| RQ01 | malformed | no text field at all | 400 | `â€”` | â€” | â€” | HELD |
| RQ02 | malformed | no creator_id | 400 | `â€”` | â€” | â€” | HELD |
| RQ03 | malformed | text is a number | 400 | `â€”` | â€” | â€” | HELD |
| RQ04 | malformed | text is a list | 400 | `â€”` | â€” | â€” | HELD |
| RQ05 | malformed | text is null | 400 | `â€”` | â€” | â€” | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `â€”` | â€” | â€” | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `â€”` | â€” | â€” | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `â€”` | â€” | â€” | HELD |
| RQ09 | malformed | body is empty | 400 | `â€”` | â€” | â€” | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `â€”` | â€” | â€” | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `â€”` | â€” | â€” | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `â€”` | â€” | â€” | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4d627c66-8acc-48ae-b137-c7743c5a7ef9` | human | 0.211 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad6b7272-8bf4-4c5b-9d8c-0cacbbef64d3` | human | 0.211 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ae5cfdc-ba84-4cc8-b85f-38328168ada8` | human | 0.211 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `51896b9d-da05-488e-bc6c-337a008ac426` | human | 0.211 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6366287d-97d5-4bf4-be00-9e55620ee747` | human | 0.211 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f54fcf91-054d-4891-95e6-6f103117976b` | human | 0.211 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `522638b5-b95b-4339-a1be-174c9307b8e0` | human | 0.211 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5799b955-a1ad-4dad-aa08-09f24dd37719` | human | 0.211 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `38fea0a4-ce6b-450f-af7d-9ed2ff6cef37` | human | 0.211 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8d5f01d5-c91a-4bd2-bc06-4f3728023cd9` | human | 0.211 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `â€”` | â€” | â€” | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `â€”` | â€” | â€” | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README â€” the ones that show something, not the ten easiest.

### EV01 â€” `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "02533e55-9085-44f8-b8fa-41ce7a9d85ad",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.27105,
  "model_score": 0.1635,
  "style_score": 0.3786,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### EV02 â€” `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f7b62fa2-f596-44f8-9fe3-55a518cc6ff5",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.39160000000000006,
  "model_score": 0.5943,
  "style_score": 0.1889,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 â€” `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "9f4fe297-ac15-4597-8ecd-59c07db41042",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.49560000000000004,
  "model_score": 0.6662,
  "style_score": 0.325,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 â€” `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "32e1c9e2-869b-4c7a-8af8-e2e30d3b586b",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.495,
  "model_score": 0.6114,
  "style_score": 0.3786,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 â€” `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "fa8d6823-c87d-4c11-a239-97c558d49003",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.304,
  "model_score": 0.3212,
  "style_score": 0.2868,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### EV06 â€” `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "57d34db1-0a8a-48e5-8bf9-d58c1b656a01",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.34885,
  "model_score": 0.5727,
  "style_score": 0.125,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### EV07 â€” `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "5cfec238-4b7e-4989-9bcd-b11361a5dc68",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5487500000000001,
  "model_score": 0.5862,
  "style_score": 0.5113,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 â€” `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d82ec795-3b6c-4426-bcd4-ab22d9347533",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.29345,
  "model_score": 0.2452,
  "style_score": 0.3417,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### EV09 â€” `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "a403fcd6-4a99-416f-8bf6-a87f113b0a3c",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5057,
  "model_score": 0.7042,
  "style_score": 0.3072,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 â€” `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "541549b8-934b-4854-81c7-e1de7304b876",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.71305,
  "model_score": 0.9792,
  "style_score": 0.4469,
  "label": "This writing is likely AI-generated.",
  "error": null,
  "verdict": ""
}
```

### FP01 â€” `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "21b99219-0ede-4d34-b344-4f58768c2712",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.47955000000000003,
  "model_score": 0.6175,
  "style_score": 0.3416,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 â€” `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "43bc36d9-42b9-4408-949e-f0868ebe49f7",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5722,
  "model_score": 0.7387,
  "style_score": 0.4057,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 â€” `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "34c12ace-c17f-4b92-9b84-75b4bb11c915",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.58855,
  "model_score": 0.8051,
  "style_score": 0.372,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 â€” `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "ed6fcbdf-3582-4905-8749-a9a87f4b7604",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5877,
  "model_score": 0.8329,
  "style_score": 0.3425,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 â€” `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "cd20b1ba-9ac2-41ce-bba7-926599556b53",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.628,
  "model_score": 0.8005,
  "style_score": 0.4555,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 â€” `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "1d8c092a-3b8e-4425-9755-b0495f458ba8",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5981,
  "model_score": 0.8814,
  "style_score": 0.3148,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 â€” `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "9e4671de-7338-4adc-ac2c-ccaabc085ffc",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6209,
  "model_score": 0.8816,
  "style_score": 0.3602,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 â€” `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0448226c-fa03-46dc-9ac9-a709504f96b7",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.39449999999999996,
  "model_score": 0.3223,
  "style_score": 0.4667,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 â€” `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "1a5a3d82-8208-41b6-bd38-22174a1437d2",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3246,
  "model_score": 0.4625,
  "style_score": 0.1867,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### PI02 â€” `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "842c8335-50d5-43dd-89dc-e7b76e1bba79",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.20895,
  "model_score": 0.2044,
  "style_score": 0.2135,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### PI03 â€” `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "f1d557fb-39a5-47b8-b356-e3382b2d0489",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.45280000000000004,
  "model_score": 0.5943,
  "style_score": 0.3113,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 â€” `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "2874ed6e-106b-48dd-bfd8-1542d9dda143",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.42785,
  "model_score": 0.4998,
  "style_score": 0.3559,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 â€” `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "2d5d74e6-0f09-4e49-bbc1-6a6ab16fbffd",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.56235,
  "model_score": 0.6401,
  "style_score": 0.4846,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 â€” `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c2fd8869-ec49-4c15-b9c7-e8545d0d1d84",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4511,
  "model_score": 0.5583,
  "style_score": 0.3439,
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 â€” `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 â€” `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 â€” `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "5a83d882-8f73-4b7a-b62c-3ec70ce7ea88",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.32535,
  "model_score": 0.0,
  "style_score": 0.6507,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### MF04 â€” `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 â€” `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "fa1491de-cfae-4ded-9b6e-36f3996a159f",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.66545,
  "model_score": 0.9976,
  "style_score": 0.3333,
  "label": "This writing is likely AI-generated.",
  "error": null,
  "verdict": ""
}
```

### MF06 â€” `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 â€” `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "301d1cd2-572a-4c69-b651-6ebfe735f4f1",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.80235,
  "model_score": 0.9064,
  "style_score": 0.6983,
  "label": "This writing is likely AI-generated.",
  "error": null,
  "verdict": ""
}
```

### MF08 â€” `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "b30ada21-87ad-4f50-a064-82a8189f0013",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.7865500000000001,
  "model_score": 0.9876,
  "style_score": 0.5855,
  "label": "This writing is likely AI-generated.",
  "error": null,
  "verdict": ""
}
```

### RQ01 â€” `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 â€” `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 â€” `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 â€” `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 â€” `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 â€” `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 â€” `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 â€” `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 â€” `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 â€” `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 â€” `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 â€” `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4d627c66-8acc-48ae-b137-c7743c5a7ef9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "ad6b7272-8bf4-4c5b-9d8c-0cacbbef64d3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "1ae5cfdc-ba84-4cc8-b85f-38328168ada8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "51896b9d-da05-488e-bc6c-337a008ac426",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "6366287d-97d5-4bf4-be00-9e55620ee747",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "f54fcf91-054d-4891-95e6-6f103117976b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "522638b5-b95b-4339-a1be-174c9307b8e0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "5799b955-a1ad-4dad-aa08-09f24dd37719",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "38fea0a4-ce6b-450f-af7d-9ed2ff6cef37",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "8d5f01d5-c91a-4bd2-bc06-4f3728023cd9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.21135,
  "model_score": 0.0287,
  "style_score": 0.394,
  "label": "This writing is likely human-written.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 â€” `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
