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
| Greater than 0.35 and less than 0.65 | `unsure` | We cannot confidently determine whether this writing was written by a human or AI. |
| 0.65–1.00 | `ai` | This writing is likely AI-generated. |

**Why I worded the unsure label this way:**

I chose wording that communicates uncertainty without making an unsupported accusation. The system cannot always reliably distinguish human-written content from AI-generated content, so the unsure label avoids presenting an uncertain prediction as a fact.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

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

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



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
