# Milestone 1: System Design and Signal Understanding

## Activity 1: Text Flow

The Provenance Guard system follows these steps when a user submits writing:

1. The website sends the user's writing (`text`) and identifier (`creator_id`) to the `POST /submit` endpoint.
2. `detector.py` analyzes the writing using its local language model.
3. `stylometry.py` measures writing-style characteristics, such as sentence-length variation, vocabulary variety, and punctuation.
4. `scoring.py` combines the two signals into a confidence score.
5. The system converts the confidence score into one of three reader-friendly labels: high-confidence AI, high-confidence human, or unsure.
6. `audit.py` records the submission and its decision.
7. The service returns the `content_id`, prediction, confidence score, and label to the website.

## Activity 2: Understanding the Two Signals

Provenance Guard uses two different signals to evaluate submitted writing.

### Signal 1: Detector (`detector.py`)

- **What it measures:**  Uses a local language model to analyze text and measure perplexity.
- **Why it matters:** Text patterns may differ between human-written and AI-generated writing.
- **Blind spot:** It can mistakenly classify human writing as AI-generated and cannot reliably establish who actually wrote a piece of text.

### Signal 2: Stylometry (`stylometry.py`)

- **What it measures:** Writing-style characteristics, including sentence-length variation, vocabulary variety, and punctuation.
- **Why it matters:** These characteristics provide additional evidence about the writing style.
- **Blind spot:** Human and AI writing can share similar stylistic characteristics. For example, formal human writing may have consistent sentence lengths and repetitive vocabulary.

## Activity 3: False-Positive Scenario

A false positive occurs when the system incorrectly identifies human-written content as AI-generated.

For example, a student writes an essay independently, but Provenance Guard returns:

- **Prediction:** AI-generated
- **Confidence:** 0.92
- **Label:** High-confidence AI

The student can challenge this decision by submitting an appeal through the `POST /appeal` endpoint.

The appeal request includes:

- `content_id`: Identifies the original submission.
- `reasoning`: Explains why the writer believes the decision is incorrect.

After receiving the appeal, the system records it and changes the submission status to `under_review`. The system does not automatically re-check the writing.

## Activity 4: Endpoint Contracts

### Endpoint 1: POST /submit

This endpoint receives writing submitted for analysis.

**Request fields:**

| Field | Description |
|---|---|
| `text` | The actual writing submitted for analysis. |
| `creator_id` | Identifies the person submitting the writing. |

**Response fields:**

| Field | Description |
|---|---|
| `content_id` | Unique identifier for the submitted content. |
| `prediction` | The system's prediction about the writing. |
| `confidence` | The confidence score associated with the prediction. |
| `label` | Reader-friendly explanation of the result. |

### Endpoint 2: POST /appeal

This endpoint allows a writer to challenge a decision.

**Request fields:**

| Field | Description |
|---|---|
| `content_id` | Identifies the original submission. |
| `reasoning` | Explains why the writer disagrees with the result. |

**System response:**

The system records the appeal, changes the submission status to `under_review`, and confirms that the appeal was received.
