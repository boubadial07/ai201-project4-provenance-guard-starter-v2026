# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

When a user submits writing, Provenance Guard follows these steps:

1. The website sends the submitted text and creator ID to the `POST /submit` endpoint.
2. `detector.py` analyzes the text using a local GPT-2 language model and calculates a model signal based on text predictability.
3. `stylometry.py` analyzes writing characteristics, including sentence-length variation, vocabulary variety, and punctuation density.
4. `scoring.py::combine_signals` combines the model signal and style signal using a weighted average.
5. The combined score is passed to `scoring.py::score_to_label`, which assigns one of three outcomes: high-confidence AI, high-confidence human, or unsure.
6. `audit.py` records the submission, signal scores, combined score, prediction, label, and decision status.
7. The service returns the content ID, prediction, confidence score, individual signal scores, and reader-friendly label to the website.

---

## Signals and Scoring

### Milestone 4 calibration results

I tested four deliberately selected writing samples: clearly AI-generated, clearly human-written, formal human writing, and lightly edited AI-generated writing.

| Input | Model score | Style score | Combined score | Prediction |
|---|---:|---:|---:|---|
| Clearly AI | 0.7719 | 0.3002 | 0.63039 | Unsure |
| Clearly human | 0.8341 | 0.3695 | 0.69472 | AI |
| Formal human | 0.4154 | 0.3429 | 0.39365 | Unsure |
| Lightly edited AI | 0.8100 | 0.3623 | 0.67569 | AI |

**What surprised me:**

The clearly human sample received a higher model score than the clearly AI sample and was classified as AI-generated. The clearly AI sample was classified as unsure because the style signal lowered the combined score.

These results show that the current detector and scoring configuration do not reliably distinguish all four writing categories. The results also demonstrate why both signal scores must be recorded for further evaluation.

### Weighting experiment: 70/30 versus 50/50

After the initial calibration, I tested a more balanced weighting configuration. I changed the model and style weights from 70/30 to 50/50 while keeping the classification thresholds unchanged.

| Input | 70/30 score | 70/30 prediction | 50/50 score | 50/50 prediction |
|---|---:|---|---:|---|
| Clearly AI | 0.63039 | Unsure | 0.53605 | Unsure |
| Clearly human | 0.69472 | AI | 0.60180 | Unsure |
| Formal human | 0.39365 | Unsure | 0.37915 | Unsure |
| Lightly edited AI | 0.67569 | AI | 0.58615 | Unsure |

### Combining rule

The combining rule is implemented in `scoring.py::combine_signals`.

It uses a weighted average of the model signal and style signal. The weights are configured in `config.py`:

- Model signal: 50% (`WEIGHT_MODEL_SIGNAL = 0.5`)
- Style signal: 50% (`WEIGHT_STYLE_SIGNAL = 0.5`)

The formula is:

`combined_score = (0.50 × model_score) + (0.50 × style_score)`

The classification thresholds are:

- **0.00–0.35:** High-confidence human
- **Above 0.35 and below 0.65:** Unsure
- **0.65–1.00:** High-confidence AI

Both signals contribute equally. When they disagree, the weighted average balances their results and may produce an unsure classification.

**What I learned:**

The 50/50 configuration reduced the combined scores and prevented the intended human samples from receiving high-confidence AI classifications. However, both AI-intended samples also received unsure classifications.

This experiment demonstrates a trade-off between reducing false positives and confidently identifying AI-generated writing. I retained the 50/50 configuration as an experimental choice, while recognizing that more testing is needed before drawing conclusions about overall accuracy.

---

### Signal one — the model signal

**What it measures:**

The model signal uses a local GPT-2 language model to calculate text perplexity, which measures how predictable the submitted writing is. The detector converts perplexity into a score between 0 and 1.

**Why that might differ between human and AI writing:**

AI-generated writing may contain predictable word patterns because language models tend to select likely next words. Human writing may contain more unusual word choices and less predictable sentence structures.

**What it can't see:**

Predictability does not prove authorship. Plain, ordinary human writing, including writing by people using a second language, can receive high AI-likelihood scores. The detector cannot reliably determine who actually wrote the text.

### Signal two — the style signal

**What it measures:**

The style signal analyzes three surface-level writing characteristics:

1. **Sentence-length variation:** Measures how much sentence lengths differ from one another.
2. **Type-token ratio:** Measures vocabulary variety by dividing the number of unique words by the total number of words.
3. **Punctuation density:** Measures the number of punctuation characters relative to the total number of characters.

The implementation converts these measurements into component scores and averages them equally to produce a style score between 0 and 1.

**Why that might differ between human and AI writing:**

The scoring approach treats more consistent sentence lengths and less varied vocabulary as potentially AI-like patterns. It also treats higher punctuation density as a potentially AI-like pattern. These are design assumptions used by this project, not universal rules about how humans or AI write.

**What it can't see:**

The style signal cannot understand the meaning of a text or verify who wrote it. Human and AI writing can share similar patterns, and someone can change sentence structure, vocabulary, or punctuation without changing authorship.

### The combining rule

**The rule:**

The system combines the model signal and style signal using a weighted average. The model signal has more influence on the final score, while the style signal provides additional information about writing patterns.

**The numbers:**

- Model signal: 70% (0.70)
- Style signal: 30% (0.30)

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**

For example, suppose the model signal is 0.80 and the style signal is 0.20. The model suggests AI-like writing, while the style signal suggests human-like writing.

Combined score = (0.70 × 0.80) + (0.30 × 0.20) = **0.62**.

The result falls into the unsure range because it is between 0.35 and 0.65. This demonstrates how the weighted average can produce an uncertain result when the two signals disagree.

These weights and thresholds are initial design choices and have not been scientifically validated.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

---

## Label Variants

| Score range | Guess | Label returned to the user |
|---|---|---|
| 0.00–0.35 | `human` | This writing is likely human-written. |
| >0.35 and <0.65 | `unsure` | We cannot confidently determine whether this writing was written by a human or AI. |
| 0.65–1.00 | `ai` | This writing is likely AI-generated. |

**Why I worded the unsure label this way:**

I chose wording that communicates uncertainty without making an unsupported accusation. The system cannot always reliably distinguish human-written content from AI-generated content, so the unsure label avoids presenting an uncertain prediction as a fact. It also recognizes that a person may have written every word themselves.

---

### Sample Run

#### 1. Submit writing

I submitted a paragraph through `POST /submit`. The system returned:

```json
{
  "combined_score": 0.6604,
  "confidence": 0.6604,
  "content_id": "ca64f988-9b1e-49e6-a88e-4f23642a80ad",
  "guess": "ai",
  "label": "This writing is likely AI-generated.",
  "model_score": 0.8951,
  "style_score": 0.4257
}
```

#### 2. Submit an appeal

I used the returned `content_id` to submit an appeal through `POST /appeal`.

The API returned:

```json
{
  "content_id": "ca64f988-9b1e-49e6-a88e-4f23642a80ad",
  "message": "Your appeal has been received and is under review.",
  "status": "under_review"
}
```

#### 3. Verify the audit log

I checked `GET /log` and confirmed that the original decision remained recorded with status `decided`. A separate appeal event appeared with the same `content_id`, the writer's reasoning, and status `under_review`.

This confirmed that appeals are recorded without deleting or replacing the original decision.
**A submission**

**Request:**

```json
{
  "text": "Yesterday was exhausting. I missed the bus, spilled coffee on my shirt, and arrived late. Honestly, what a morning! I finally got home and relaxed.",
  "creator_id": "test-user-001"
}
```

**Response:**

```json
{
  "combined_score": 0.48983,
  "confidence": 0.48983,
  "content_id": "daa971fb-a25e-45a1-bfbc-94fe00b75ed8",
  "guess": "unsure",
  "label": "We cannot confidently determine whether this writing was written by a human or AI.",
  "model_score": 0.5696,
  "style_score": 0.3037
}
```

**An appeal**

**Request:**
{
  "content_id": "daa971fb-a25e-45a1-bfbc-94fe00b75ed8",
  "reasoning": "I wrote this text myself and would like the decision reviewed."
}


**Response:**
{
  "content_id": "daa971fb-a25e-45a1-bfbc-94fe00b75ed8",
  "message": "Your appeal has been received and is under review.",
  "status": "under_review"
}


**What the log shows afterwards**

**Request:**

```powershell
$logResponse = Invoke-RestMethod -Uri "http://127.0.0.1:5000/log" -Method Get
$logResponse | ConvertTo-Json -Depth 10
```

**Relevant log entries:**

```json
{
  "count": 13,
  "entries": [
    {
      "content_id": "daa971fb-a25e-45a1-bfbc-94fe00b75ed8",
      "creator_id": "test-user-001",
      "guess": "unsure",
      "model_score": 0.5696,
      "style_score": 0.3037,
      "combined_score": 0.48983,
      "status": "decided"
    },
    {
      "content_id": "daa971fb-a25e-45a1-bfbc-94fe00b75ed8",
      "creator_id": "test-user-001",
      "event": "appeal",
      "reasoning": "I wrote this text myself and would like the decision reviewed.",
      "status": "under_review"
    }
  ]
}
```

**What this demonstrates:**

The audit log preserves the original submission decision and records the appeal as a separate event. The appeal is marked `under_review` without automatically changing the original classification.

---

## How I Used AI

### Moment 1: Building the stylometry signal

I asked AI to help me understand how to calculate sentence-length variation, type-token ratio, and punctuation density in Python. AI explained the calculations and suggested ways to normalize the measurements into scores. I reviewed the suggestions, implemented the functions in `stylometry.py`, and tested them with sample paragraphs. I also adjusted the scoring formula to include all three characteristics.

### Moment 2: Combining signals and implementing appeals

I asked AI to explain how to combine the model and style signals and how to implement the appeal workflow. AI suggested a weighted-average approach and helped me understand how to record appeal events in the audit log. I implemented the logic in `scoring.py` and `app.py`, selected the initial 70/30 weights, and tested the submission and appeal endpoints using PowerShell. I reviewed the actual JSON responses and verified that appeals were recorded with the `under_review` status.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why these numbers and not others:**

I chose 10 requests per minute to allow legitimate writers to submit and revise their work without unnecessary interruptions while limiting automated scripts that repeatedly submit variations to probe the detector. The daily limit of 200 provides room for normal usage while restricting sustained automated activity.

**What a caller counts as:**

Requests are counted by `creator_id` when it is provided. If a valid creator ID is unavailable, the system falls back to the caller's IP address.

**The run of status codes when I pushed past it:**

10 requests returned HTTP 200 (accepted), followed by 5 requests returning HTTP 429 (rate limited).

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

```json
[
  {
    "creator_id": "attacker_EV01",
    "content_id": "566aa29e-8a5b-4572-a372-720111f4b2ad",
    "guess": "human",
    "combined_score": 0.27105,
    "status": "decided"
  },
  {
    "creator_id": "attacker_EV09",
    "content_id": "d5eac682-5fb2-48ee-8314-bc42948cc9f3",
    "guess": "unsure",
    "combined_score": 0.5057,
    "status": "decided"
  },
  {
    "creator_id": "attacker_FP03",
    "content_id": "3194ef55-55e7-4aa9-8895-bcd0c11026e6",
    "guess": "unsure",
    "combined_score": 0.58855,
    "status": "decided"
  },
  {
    "creator_id": "attacker_FP05",
    "content_id": "c42325ac-d021-452d-80b7-513fc1b2d3ce",
    "guess": "unsure",
    "combined_score": 0.628,
    "status": "decided"
  },
  {
    "creator_id": "attacker_PI05",
    "content_id": "23cbc198-80c1-409c-9de1-75fabe9808d7",
    "guess": "unsure",
    "combined_score": 0.56235,
    "status": "decided"
  },
  {
    "creator_id": "attacker_MF06",
    "content_id": "7bedcf87-6346-4a8d-a8e0-969ea3f6b3be",
    "guess": "ai",
    "combined_score": 0.8318,
    "status": "decided"
  },
  {
    "creator_id": "attacker_MF08",
    "content_id": "4d64a6dc-4a46-45d0-bc2d-fc56239c73cc",
    "guess": "ai",
    "combined_score": 0.78655,
    "status": "decided"
  },
  {
    "creator_id": "attacker_flood",
    "content_id": "e6192710-b0da-4aba-adba-8c58e2f73499",
    "guess": "human",
    "combined_score": 0.21135,
    "status": "decided"
  },
  {
    "creator_id": "attacker_flood",
    "guess": null,
    "status": "rejected"
  },
  {
    "creator_id": "attacker_flood",
    "guess": null,
    "status": "rejected"
  }
]

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:
The worst outcome was RQ07, which sent a JSON array instead of the expected JSON object. The service returned HTTP 500 because the route attempted to call .get() on a list, resulting in an AttributeError. This was a failure at the route/input-validation stage, before the scoring functions could process the request. The service should validate the incoming JSON structure and return a controlled HTTP 400 response instead of an internal server error.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing | No more than 1 high-confidence AI label out of 10 | 0 | 0 | 0 | Passed |
| 2. Score spread | Difference of at least 0.20 | 0.0995 | 0.0995 | 0.0995 | Missed |
| 3. Label coverage | All 3 labels reachable | Unsure only | Unsure only | Unsure only | Missed |
| 4. Appeal process | All valid appeals recorded as under_review | 1 manual test passed | Not tested | Not tested | Partially verified |
| 5. Bad input handling | All 3 invalid inputs return HTTP 400 | 3/3 returned 400 | 3/3 returned 400 | 3/3 returned 400 | Passed |

### Criterion 4 — Appeal process

**Target:** A valid appeal changes the submission status to `under_review` in every test.

I tested the appeal process manually. First, I submitted a valid text through `/submit` and received a `content_id`. I then sent an appeal to `/appeal` using that ID and a written explanation.

The endpoint returned HTTP 200 and confirmed that the appeal was received. I also checked the audit log and verified that it contained both the original submission event (`decided`) and the appeal event (`under_review`) for the same content ID.

**Result:** The manual appeal test passed. The appeal event was successfully recorded in the audit log.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

### Criterion 5 — Bad input handling (Trial 1)

Source: `results/run_2026-11-11_2232_milestone3_bad_input.md`

Function: `run_eval.py::main`

The following three test cases returned HTTP 400 as expected:

```json
[
  {
    "status": 400,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "sent": "{\"text\": \"This is a valid test submission.\"}"
  }
]
```

Result: **3 out of 3 invalid inputs returned HTTP 400.** Criterion 5 passed in all three trials.

### Criterion 2 — Score spread (Trial 1)

Source: `run_eval.py` evaluation report

The average confidence scores were:

- Human samples: 0.4313
- AI-generated samples: 0.5308
- Absolute difference: 0.0995

Target: At least 0.20.

Result: **Missed.** The observed difference of 0.0995 was below the required 0.20 threshold.

### Criterion 3 — Label coverage (Trial 1)

Source: `results/run_2026-11-11_2232_milestone3_bad_input.md`

Function: `run_eval.py::main`

The three test samples produced these labels:

```json
[
  {
    "guess": "unsure",
    "confidence": 0.58245
  },
  {
    "guess": "unsure",
    "confidence": 0.5297
  },
  {
    "guess": "unsure",
    "confidence": 0.5642
  }
]
```

Result: **Missed.** All three samples received the `unsure` label. The evaluation did not demonstrate that all three required labels were reachable.

### Criterion 1 — My own writing (Trial 1)

Source: `results/run_2026-11-11_2232_milestone3_bad_input.md`

Function: `run_eval.py::main`

The 10 personal writing samples produced the following results:

```json
{
  "total_samples": 10,
  "high_confidence_ai": 0,
  "human": 2,
  "unsure": 8
}
```

Result: **Passed.** None of the 10 samples received a high-confidence AI label, meeting the target of no more than one false positive.

### Criterion 4 — Appeal process (Manual Test)

Source: Manual test using the `/submit`, `/appeal`, and `/log` endpoints.

The appeal process was tested using a valid submission with content ID:

`226fbf9c-ce0a-451c-891b-69f157021ad9`

The appeal request returned HTTP 200 with the following response:

```json
{
  "content_id": "226fbf9c-ce0a-451c-891b-69f157021ad9",
  "status": "under_review",
  "message": "Your appeal has been received and is under review."
}
```

The audit log was also checked and confirmed that a separate appeal event was recorded for the same content ID and creator ID.

Result: **One manual appeal test passed.** The appeal was successfully recorded and its status changed to `under_review`. The full three-trial acceptance target has not yet been verified.

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

### Diagnosis 1 — Evasion attacks

EV01–EV09 bypassed the AI classification by receiving either a human or unsure label. The failures involved both signals. Some attacks manipulated writing-style characteristics, such as word variety and sentence-length spread, while others affected the model signal through unusual words or short text. The combining rule weighted both signals, allowing manipulated scores to fall below the AI classification threshold. The label mapping then returned human or unsure instead of AI.

### Diagnosis 2 — Request validation failures

In the baseline run, MF02 and RQ07 caused HTTP 500 errors at the route stage. MF02 submitted a single-character text that reached the model signal, which raised a ValueError because the text was too short. RQ07 submitted a JSON array instead of an object, causing an AttributeError when the route attempted to call `.get()`. I addressed both failures by adding payload-type validation and minimum text-length validation. In the after-fix run, both inputs returned controlled HTTP 400 responses instead of HTTP 500 errors.

### Diagnosis 3 — Malformed text handling

MF04 and MF06 exposed weaknesses in text validation. Punctuation-only and emoji-only inputs were initially accepted and passed to the scoring functions. I added an alphanumeric-character validation check, which now rejects these inputs with HTTP 400. MF03 was labeled as a control-character attack, but inspection of the original CSV showed that its payload was actually "test red", which is ordinary text. Therefore, its HTTP 200 response is expected.

### Diagnosis 4 — Rate limiting

The flood attack demonstrated that rate limiting worked as intended. The first 10 requests were accepted, while the next two received HTTP 429 responses. The limiter successfully restricted repeated submissions from the same creator.

---

## The Improvement

**What I changed:**

I improved request validation in `app.py` by checking that incoming requests contain a valid JSON object, that text is a nonempty string with at least 10 characters, that the text contains at least one letter or number, and that `creator_id` is a nonempty string. I also added rejection logging through `audit.log_rejection()` so invalid submissions are recorded with their rejection reasons and HTTP status codes.

**Which diagnosis pointed at it:**

The baseline attack run exposed two HTTP 500 responses caused by malformed requests, as well as malformed text inputs that were not being rejected consistently. These results showed that the submission endpoint needed stronger input validation and better rejection logging.

### Baseline vs. After-Fix Comparison

Both runs used the same 56-attack test set.

| HTTP Status | Baseline — Nov 8 | After Fixes — Nov 13 | Change |
|---|---:|---:|---|
| HTTP 200 | 40 | 38 | -2 |
| HTTP 400 | 12 | 16 | +4 |
| HTTP 429 | 2 | 2 | No change |
| HTTP 500 | 2 | 0 | -2 |
| **Total** | **56** | **56** | **Same test size** |

**Measured improvement:**

- HTTP 500 errors decreased from 2 to 0.
- Invalid requests that previously caused server errors now receive controlled HTTP 400 responses.
- Rate limiting continued to work, accepting the first 10 requests and rejecting the next 2 with HTTP 429.
- The scoring system's evasion weaknesses remain unresolved; request validation does not prevent adversarial writing from receiving human or unsure classifications.

**Evidence:**
- Baseline: `results/attack_run_2026-11-08_1008.md`
- After fixes: `results/attack_run_2026-11-13_2023_after_audit_fix.md`

## Attack Run — After (Validation Fixes)

After reviewing the baseline attack results, I improved request validation in `app.py`.

I added validation to ensure that:
- The request body must be a valid JSON object.
- Text must be a nonempty string.
- Text must contain at least 10 characters.
- Text must contain at least one letter or number.
- Invalid requests receive controlled HTTP 400 responses instead of server errors.

### Audit logging verification

I verified the audit export in `results/audit_extract_after_audit_fix.json`.

The export contained 200 records, including:

- 159 successful decision records, identified by `status: decided`.
- 1 appeal record.
- 40 rejected request records, identified by `event: rejected`.

The 40 rejection records included:

| Rejection reason | Count |
|---|---:|
| Invalid payload | 12 |
| Invalid text | 18 |
| Text too short | 3 |
| Invalid creator ID | 5 |
| Rate limited | 2 |
| **Total** | **40** |

Successful decision records contain timestamps, creator IDs, content IDs, model scores, style scores, combined scores, labels, and statuses. Rejection records contain timestamps, creator IDs, reasons, error messages, HTTP status codes, and rejection statuses where applicable.

The two rate-limited requests were recorded with the reason `rate_limited`.

This verifies that the application records both successful decisions and rejected requests, providing evidence for reviewing submissions and diagnosing failures.

### Post-fix results

I reran all 56 attacks using `python run_attacks.py --set .\attack_set`.

- HTTP 200: 38
- HTTP 400: 16
- HTTP 429: 2
- HTTP 500: 0

Both original HTTP 500 failures were eliminated:
- MF02: Single-character input now returns HTTP 400.
- RQ07: JSON array input now returns HTTP 400.

MF04 (punctuation-only) and MF06 (emoji-only) also now return HTTP 400.

MF03 returned HTTP 200 because inspection of the original attack data showed its payload was ordinary text ("test red"), not control characters.

The flood test continued to work as expected: 10 requests were accepted and the next two were rate limited with HTTP 429.

Attack report: `results/attack_run_2026-11-10_1037.md`

### Automated test discovery

I ran `pytest -q`, but pytest reported that no tests were collected. I also searched the project for test files outside the virtual environment and found none. Therefore, this submission's verification is based on the documented manual tests, acceptance-criteria trials, attack runs, and audit-log evidence rather than a passing automated test suite.

**Did it help, and how do I know:**

The validation fixes improved the service's handling of malformed requests. In the baseline run, two attacks caused HTTP 500 errors (MF02 and RQ07). After the fixes, both returned controlled HTTP 400 responses, and the total number of HTTP 500 errors dropped from 2 to 0.

The fixes also prevented punctuation-only and emoji-only inputs from reaching the scoring functions. Rate limiting continued to reject excessive requests with HTTP 429.

However, the fixes did not solve the evasion attacks (EV01–EV09), which continued to receive human or unsure classifications. This shows that input validation improved request handling, but the scoring system still needs improvement.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

### Criterion 2 — Score spread

The original target required the average confidence scores for 10 human-written samples and 10 AI-generated samples to differ by at least 0.20 in each of the three trials.

The observed difference was 0.0995, which did not meet the target.

This indicates that the model and style signals did not create enough separation between the two groups. The current weighted scoring approach produces overlapping confidence scores, making it difficult to distinguish human-written content from AI-generated content reliably.

A possible improvement would be to investigate how the two signals are calibrated and whether their individual scores provide enough separation before combining them.

### Criterion 3 — Label coverage

The target required all three labels — High-confidence AI, High-confidence human, and Unsure — to be reachable, with at least one example of each label in every trial.

The evaluation did not meet this target. All three test samples received the `unsure` label across the three trials.

This suggests that the test samples produced confidence scores within the current unsure range. Although the system successfully returned a label for each sample, it did not demonstrate that the high-confidence AI and high-confidence human labels were reachable.

A possible improvement would be to review the scoring thresholds and test samples while preserving the original acceptance criteria.

## The trade I'd make if this ran for real:

I would prioritize reducing false accusations against human writers, even if that means allowing some AI-generated content to pass undetected. Writers should not be penalized by an unreliable detector, while organizations deploying this system should be responsible for funding ongoing testing, calibration, and human review.


<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
