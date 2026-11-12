# Run log — milestone3_bad_input

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-11 22:32

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. score spread |  |   |   |   |  |
| 3. label coverage |  |   |   |   |  |
| 5. bad input handling |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4824,
    "model_score": 0.7311,
    "style_score": 0.2337,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Hello, my name is Boubacar Diallo. From a young age, I've had a strong"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3175,
    "model_score": 0.3065,
    "style_score": 0.3285,
    "label": "This writing is likely human-written.",
    "sent": "In addition to my academic journey, I'm also getting some certificatio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37725,
    "model_score": 0.4961,
    "style_score": 0.2584,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "What motivated me to keep learning new things is that technology is ev"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.53505,
    "model_score": 0.598,
    "style_score": 0.4721,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "A challenge I experienced while learning something new was using Cisco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.42700000000000005,
    "model_score": 0.394,
    "style_score": 0.46,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "In the next five years, I see myself thring, improving and working in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37060000000000004,
    "model_score": 0.3639,
    "style_score": 0.3773,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I will never forget the first day I got in the U.S speciffically in Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4696,
    "model_score": 0.6484,
    "style_score": 0.2908,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I'm proud of finishing my Bachelor's degree and building a family. Not"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40385,
    "model_score": 0.4992,
    "style_score": 0.3085,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology has made people's lives better and more complicated. People"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34735,
    "model_score": 0.476,
    "style_score": 0.2187,
    "label": "This writing is likely human-written.",
    "sent": "Having a happy family and helping others mean success to me. Finacial "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4824,
    "model_score": 0.7311,
    "style_score": 0.2337,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Hello, my name is Boubacar Diallo. From a young age, I've had a strong"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3175,
    "model_score": 0.3065,
    "style_score": 0.3285,
    "label": "This writing is likely human-written.",
    "sent": "In addition to my academic journey, I'm also getting some certificatio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37725,
    "model_score": 0.4961,
    "style_score": 0.2584,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "What motivated me to keep learning new things is that technology is ev"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.53505,
    "model_score": 0.598,
    "style_score": 0.4721,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "A challenge I experienced while learning something new was using Cisco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.42700000000000005,
    "model_score": 0.394,
    "style_score": 0.46,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "In the next five years, I see myself thring, improving and working in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37060000000000004,
    "model_score": 0.3639,
    "style_score": 0.3773,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I will never forget the first day I got in the U.S speciffically in Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4696,
    "model_score": 0.6484,
    "style_score": 0.2908,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I'm proud of finishing my Bachelor's degree and building a family. Not"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40385,
    "model_score": 0.4992,
    "style_score": 0.3085,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology has made people's lives better and more complicated. People"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34735,
    "model_score": 0.476,
    "style_score": 0.2187,
    "label": "This writing is likely human-written.",
    "sent": "Having a happy family and helping others mean success to me. Finacial "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4824,
    "model_score": 0.7311,
    "style_score": 0.2337,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Hello, my name is Boubacar Diallo. From a young age, I've had a strong"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3175,
    "model_score": 0.3065,
    "style_score": 0.3285,
    "label": "This writing is likely human-written.",
    "sent": "In addition to my academic journey, I'm also getting some certificatio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37725,
    "model_score": 0.4961,
    "style_score": 0.2584,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "What motivated me to keep learning new things is that technology is ev"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.53505,
    "model_score": 0.598,
    "style_score": 0.4721,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "A challenge I experienced while learning something new was using Cisco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.42700000000000005,
    "model_score": 0.394,
    "style_score": 0.46,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "In the next five years, I see myself thring, improving and working in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37060000000000004,
    "model_score": 0.3639,
    "style_score": 0.3773,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I will never forget the first day I got in the U.S speciffically in Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4696,
    "model_score": 0.6484,
    "style_score": 0.2908,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I'm proud of finishing my Bachelor's degree and building a family. Not"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40385,
    "model_score": 0.4992,
    "style_score": 0.3085,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology has made people's lives better and more complicated. People"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34735,
    "model_score": 0.476,
    "style_score": 0.2187,
    "label": "This writing is likely human-written.",
    "sent": "Having a happy family and helping others mean success to me. Finacial "
  }
]
```

### score spread

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4824,
    "model_score": 0.7311,
    "style_score": 0.2337,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Hello, my name is Boubacar Diallo. From a young age, I've had a strong"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3175,
    "model_score": 0.3065,
    "style_score": 0.3285,
    "label": "This writing is likely human-written.",
    "sent": "In addition to my academic journey, I'm also getting some certificatio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37725,
    "model_score": 0.4961,
    "style_score": 0.2584,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "What motivated me to keep learning new things is that technology is ev"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.53505,
    "model_score": 0.598,
    "style_score": 0.4721,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "A challenge I experienced while learning something new was using Cisco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.42700000000000005,
    "model_score": 0.394,
    "style_score": 0.46,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "In the next five years, I see myself thring, improving and working in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37060000000000004,
    "model_score": 0.3639,
    "style_score": 0.3773,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I will never forget the first day I got in the U.S speciffically in Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4696,
    "model_score": 0.6484,
    "style_score": 0.2908,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I'm proud of finishing my Bachelor's degree and building a family. Not"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40385,
    "model_score": 0.4992,
    "style_score": 0.3085,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology has made people's lives better and more complicated. People"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34735,
    "model_score": 0.476,
    "style_score": 0.2187,
    "label": "This writing is likely human-written.",
    "sent": "Having a happy family and helping others mean success to me. Finacial "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.59295,
    "model_score": 0.851,
    "style_score": 0.3349,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology continues to transform the way people live and work. New to"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5297,
    "model_score": 0.7191,
    "style_score": 0.3403,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Cybersecurity is an important responsibility for individuals and organ"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.6717,
    "style_score": 0.3283,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Education provides individuals with opportunities to develop knowledge"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5074000000000001,
    "model_score": 0.6177,
    "style_score": 0.3971,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Artificial intelligence is changing many industries by automating repe"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5056,
    "model_score": 0.7032,
    "style_score": 0.308,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Professional development plays an important role in career growth. Emp"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5116,
    "model_score": 0.7452,
    "style_score": 0.278,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Strong family relationships are built through communication, patience,"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.49955000000000005,
    "model_score": 0.6508,
    "style_score": 0.3483,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Sports teach valuable lessons that extend beyond physical fitness. Par"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.49445,
    "model_score": 0.6795,
    "style_score": 0.3094,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Managing time effectively requires individuals to understand their pri"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5577000000000001,
    "model_score": 0.7104,
    "style_score": 0.405,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Social media has created new opportunities for people to communicate a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6095,
    "model_score": 0.7999,
    "style_score": 0.4191,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Environmental sustainability requires individuals, businesses, and gov"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4824,
    "model_score": 0.7311,
    "style_score": 0.2337,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Hello, my name is Boubacar Diallo. From a young age, I've had a strong"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3175,
    "model_score": 0.3065,
    "style_score": 0.3285,
    "label": "This writing is likely human-written.",
    "sent": "In addition to my academic journey, I'm also getting some certificatio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37725,
    "model_score": 0.4961,
    "style_score": 0.2584,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "What motivated me to keep learning new things is that technology is ev"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.53505,
    "model_score": 0.598,
    "style_score": 0.4721,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "A challenge I experienced while learning something new was using Cisco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.42700000000000005,
    "model_score": 0.394,
    "style_score": 0.46,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "In the next five years, I see myself thring, improving and working in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37060000000000004,
    "model_score": 0.3639,
    "style_score": 0.3773,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I will never forget the first day I got in the U.S speciffically in Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4696,
    "model_score": 0.6484,
    "style_score": 0.2908,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I'm proud of finishing my Bachelor's degree and building a family. Not"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40385,
    "model_score": 0.4992,
    "style_score": 0.3085,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology has made people's lives better and more complicated. People"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34735,
    "model_score": 0.476,
    "style_score": 0.2187,
    "label": "This writing is likely human-written.",
    "sent": "Having a happy family and helping others mean success to me. Finacial "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.59295,
    "model_score": 0.851,
    "style_score": 0.3349,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology continues to transform the way people live and work. New to"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5297,
    "model_score": 0.7191,
    "style_score": 0.3403,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Cybersecurity is an important responsibility for individuals and organ"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.6717,
    "style_score": 0.3283,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Education provides individuals with opportunities to develop knowledge"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5074000000000001,
    "model_score": 0.6177,
    "style_score": 0.3971,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Artificial intelligence is changing many industries by automating repe"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5056,
    "model_score": 0.7032,
    "style_score": 0.308,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Professional development plays an important role in career growth. Emp"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5116,
    "model_score": 0.7452,
    "style_score": 0.278,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Strong family relationships are built through communication, patience,"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.49955000000000005,
    "model_score": 0.6508,
    "style_score": 0.3483,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Sports teach valuable lessons that extend beyond physical fitness. Par"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.49445,
    "model_score": 0.6795,
    "style_score": 0.3094,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Managing time effectively requires individuals to understand their pri"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5577000000000001,
    "model_score": 0.7104,
    "style_score": 0.405,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Social media has created new opportunities for people to communicate a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6095,
    "model_score": 0.7999,
    "style_score": 0.4191,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Environmental sustainability requires individuals, businesses, and gov"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4824,
    "model_score": 0.7311,
    "style_score": 0.2337,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Hello, my name is Boubacar Diallo. From a young age, I've had a strong"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3175,
    "model_score": 0.3065,
    "style_score": 0.3285,
    "label": "This writing is likely human-written.",
    "sent": "In addition to my academic journey, I'm also getting some certificatio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37725,
    "model_score": 0.4961,
    "style_score": 0.2584,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "What motivated me to keep learning new things is that technology is ev"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.53505,
    "model_score": 0.598,
    "style_score": 0.4721,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "A challenge I experienced while learning something new was using Cisco"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.42700000000000005,
    "model_score": 0.394,
    "style_score": 0.46,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "In the next five years, I see myself thring, improving and working in "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.37060000000000004,
    "model_score": 0.3639,
    "style_score": 0.3773,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I will never forget the first day I got in the U.S speciffically in Ne"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4696,
    "model_score": 0.6484,
    "style_score": 0.2908,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I'm proud of finishing my Bachelor's degree and building a family. Not"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40385,
    "model_score": 0.4992,
    "style_score": 0.3085,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology has made people's lives better and more complicated. People"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.34735,
    "model_score": 0.476,
    "style_score": 0.2187,
    "label": "This writing is likely human-written.",
    "sent": "Having a happy family and helping others mean success to me. Finacial "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.59295,
    "model_score": 0.851,
    "style_score": 0.3349,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology continues to transform the way people live and work. New to"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5297,
    "model_score": 0.7191,
    "style_score": 0.3403,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Cybersecurity is an important responsibility for individuals and organ"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.6717,
    "style_score": 0.3283,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Education provides individuals with opportunities to develop knowledge"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5074000000000001,
    "model_score": 0.6177,
    "style_score": 0.3971,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Artificial intelligence is changing many industries by automating repe"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5056,
    "model_score": 0.7032,
    "style_score": 0.308,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Professional development plays an important role in career growth. Emp"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5116,
    "model_score": 0.7452,
    "style_score": 0.278,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Strong family relationships are built through communication, patience,"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.49955000000000005,
    "model_score": 0.6508,
    "style_score": 0.3483,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Sports teach valuable lessons that extend beyond physical fitness. Par"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.49445,
    "model_score": 0.6795,
    "style_score": 0.3094,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Managing time effectively requires individuals to understand their pri"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5577000000000001,
    "model_score": 0.7104,
    "style_score": 0.405,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Social media has created new opportunities for people to communicate a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6095,
    "model_score": 0.7999,
    "style_score": 0.4191,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Environmental sustainability requires individuals, businesses, and gov"
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5297,
    "model_score": 0.7191,
    "style_score": 0.3403,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Cybersecurity is an important responsibility for individuals and organ"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5642,
    "model_score": 0.809,
    "style_score": 0.3194,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology is changing the way we live and work. I think it makes many"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5297,
    "model_score": 0.7191,
    "style_score": 0.3403,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Cybersecurity is an important responsibility for individuals and organ"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5642,
    "model_score": 0.809,
    "style_score": 0.3194,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology is changing the way we live and work. I think it makes many"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.58245,
    "model_score": 0.7264,
    "style_score": 0.4385,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "I enjoy playing soccer in my free time. I've always love playing socce"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5297,
    "model_score": 0.7191,
    "style_score": 0.3403,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Cybersecurity is an important responsibility for individuals and organ"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5642,
    "model_score": 0.809,
    "style_score": 0.3194,
    "label": "We cannot confidently determine whether this writing was written by a human or AI.",
    "sent": "Technology is changing the way we live and work. I think it makes many"
  }
]
```

### bad input handling

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This is a valid test submission.\"}"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This is a valid test submission.\"}"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This is a valid test submission.\"}"
  }
]
```
