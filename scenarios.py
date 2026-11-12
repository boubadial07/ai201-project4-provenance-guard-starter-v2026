"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "Hello, my name is Boubacar Diallo. From a young age, I've had a strong passion for technology, especially when it came to solving challenges like cracking codes and helping people regain access to their devices. This fascination with understanding and manipulating elctronic systems naturally led me to pursue a Bachelor's degree in Information Technology at ASU where I specialized in cybersecurity and networking.",

            "In addition to my academic journey, I'm also getting some certifications and technical training to strenghten my technical skills. Over the past several years, I’ve worked as an independent contractor with Uber. This role has really improved my problem-solving abilities, communication skills, and adaptability in dynamic environments. I alslo have a part-time job as a IT Desktop Support Technician at JP Morgan chase where I support entreprise IT refresh initiatives, dploy and configure workstations and peripherals accross corporateoffices. I troubleshoot hardware, connectivity and system configuration issues to minimize user disrutions.",

            "What motivated me to keep learning new things is that technology is evolving every day and I'd like to remain a tech savvy. This will help me in my job hunting. I also personally like to learning new concepts  and technologies.",

            "A challenge I experienced while learning something new was using Cisco Packet Tracer. In my first networking course, I was working on a project to build a home based network. I had no experience using packet tracer and the dealine was so tight. So I had to learn really quick how packet tracer work and how to use it. I did some research on the onternet, watched some videos and went through coursework document. I was able to learn the software and finally submitted my project on time.",

            "I enjoy playing soccer in my free time. I've always love playing soccer since I was a kid. Now every wednesday, I practice soccer with firends. It helps me to stay in a good shape and healthy. And when I'm playing on the field, I forget all my problems and I'm stress free. It's like a therapy for me.",

            "In the next five years, I see myself thring, improving and working in big tech company or with the government. I always dreamed to work in tech field, wether it's helping people secure their assets or developing software, that's something I enjoy doing.",

            "I will never forget the first day I got in the U.S speciffically in New York. It was a December when I came from Mali, a hot and dry weather country to New Yoek city, a freezing city in December(winter time). I remember the first wind that hit my face when I got out of the airport. I've nerver seen or experience anything like that before. It was a start of new adventure for me.",

            "I'm proud of finishing my Bachelor's degree and building a family. Not everyone can go to school full time for 4 years and work at the same time to finish his degree and being able to paying bills and taking car of his family. I did it and I'm so proud of myself. Now a happy father with 3 kids and a wife, so grateful. And I'm still learning and keeping pushing to the top. I hope to get there very soon!",

            "Technology has made people's lives better and more complicated. People are so close from a long distance thanks to technology, people can reach their loved one from different places in the world. It facilitated processing numbers and information quickly. Despite these advantages, Technology made people's lives complicated. A couple living togather in the same house, seems far away from each other because of their electronic devices and social media. Each one is scrolling through feeds. On top of that, AI is making people lazy and they don't make much efforts to work their brain. People are concerned about AI taking over their jobs. SORRY NO OFFENSE TO YOU (laugh)",

            "Having a happy family and helping others mean success to me. Finacial freedom is great but having a family is richer and priceless. Imagine leaving a job that you're doing just to be able to pay your bills and taking care of your family and come home where your kids run toword you a shout your name and hugging you, that's the best feeling ever. Being able to help others with the least you have is human. Helping each other will make life much easier for everyone."
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        "human_texts": [
            "Hello, my name is Boubacar Diallo. From a young age, I've had a strong passion for technology, especially when it came to solving challenges like cracking codes and helping people regain access to their devices. This fascination with understanding and manipulating elctronic systems naturally led me to pursue a Bachelor's degree in Information Technology at ASU where I specialized in cybersecurity and networking.",

            "In addition to my academic journey, I'm also getting some certifications and technical training to strenghten my technical skills. Over the past several years, I’ve worked as an independent contractor with Uber. This role has really improved my problem-solving abilities, communication skills, and adaptability in dynamic environments. I alslo have a part-time job as a IT Desktop Support Technician at JP Morgan chase where I support entreprise IT refresh initiatives, dploy and configure workstations and peripherals accross corporateoffices. I troubleshoot hardware, connectivity and system configuration issues to minimize user disrutions.",

            "What motivated me to keep learning new things is that technology is evolving every day and I'd like to remain a tech savvy. This will help me in my job hunting. I also personally like to learning new concepts  and technologies.",

            "A challenge I experienced while learning something new was using Cisco Packet Tracer. In my first networking course, I was working on a project to build a home based network. I had no experience using packet tracer and the dealine was so tight. So I had to learn really quick how packet tracer work and how to use it. I did some research on the onternet, watched some videos and went through coursework document. I was able to learn the software and finally submitted my project on time.",

            "I enjoy playing soccer in my free time. I've always love playing soccer since I was a kid. Now every wednesday, I practice soccer with firends. It helps me to stay in a good shape and healthy. And when I'm playing on the field, I forget all my problems and I'm stress free. It's like a therapy for me.",

            "In the next five years, I see myself thring, improving and working in big tech company or with the government. I always dreamed to work in tech field, wether it's helping people secure their assets or developing software, that's something I enjoy doing.",

            "I will never forget the first day I got in the U.S speciffically in New York. It was a December when I came from Mali, a hot and dry weather country to New Yoek city, a freezing city in December(winter time). I remember the first wind that hit my face when I got out of the airport. I've nerver seen or experience anything like that before. It was a start of new adventure for me.",

            "I'm proud of finishing my Bachelor's degree and building a family. Not everyone can go to school full time for 4 years and work at the same time to finish his degree and being able to paying bills and taking car of his family. I did it and I'm so proud of myself. Now a happy father with 3 kids and a wife, so grateful. And I'm still learning and keeping pushing to the top. I hope to get there very soon!",

            "Technology has made people's lives better and more complicated. People are so close from a long distance thanks to technology, people can reach their loved one from different places in the world. It facilitated processing numbers and information quickly. Despite these advantages, Technology made people's lives complicated. A couple living togather in the same house, seems far away from each other because of their electronic devices and social media. Each one is scrolling through feeds. On top of that, AI is making people lazy and they don't make much efforts to work their brain. People are concerned about AI taking over their jobs. SORRY NO OFFENSE TO YOU (laugh)",

            "Having a happy family and helping others mean success to me. Finacial freedom is great but having a family is richer and priceless. Imagine leaving a job that you're doing just to be able to pay your bills and taking care of your family and come home where your kids run toword you a shout your name and hugging you, that's the best feeling ever. Being able to help others with the least you have is human. Helping each other will make life much easier for everyone."
        ],
        "ai_texts": [
            "Technology continues to transform the way people live and work. New tools allow businesses to improve productivity, communicate more efficiently, and solve problems that once required significant time and resources. However, organizations must also consider the challenges associated with adopting new technologies, including security risks, training requirements, and implementation costs.",

            "Cybersecurity is an important responsibility for individuals and organizations. Strong passwords, multi-factor authentication, and regular software updates can reduce the risk of unauthorized access. Employees should also learn how to recognize suspicious emails and avoid clicking on unfamiliar links. A security strategy is most effective when technology and human awareness work together.",

            "Education provides individuals with opportunities to develop knowledge, improve their abilities, and prepare for future challenges. Learning does not end after graduation because industries continue to change. People who remain curious and willing to develop new skills are often better prepared to adapt to different professional environments.",

            "Artificial intelligence is changing many industries by automating repetitive tasks and supporting complex decision-making. Healthcare professionals can use AI tools to analyze information, while businesses can apply them to improve customer service. Despite these benefits, responsible implementation requires attention to privacy, accuracy, transparency, and human oversight.",

            "Professional development plays an important role in career growth. Employees who invest time in learning new skills can improve their performance and prepare themselves for additional responsibilities. Certifications, practical projects, mentorship, and workplace experience are all valuable ways to strengthen professional knowledge.",

            "Strong family relationships are built through communication, patience, and mutual respect. Spending quality time together helps family members develop trust and understand each other's needs. Although work and daily responsibilities can make it difficult to maintain a balance, making time for loved ones contributes to a healthier and more supportive home environment.",

            "Sports teach valuable lessons that extend beyond physical fitness. Participating in team activities encourages communication, discipline, cooperation, and accountability. Players must learn to support one another, accept different responsibilities, and work toward a shared objective. These qualities can also be useful in professional and personal situations.",

            "Managing time effectively requires individuals to understand their priorities and organize their responsibilities. Creating a realistic schedule can help reduce unnecessary stress and improve productivity. It is also important to recognize that unexpected situations may occur, making flexibility an essential part of successful planning.",

            "Social media has created new opportunities for people to communicate and exchange information. Individuals can maintain relationships across long distances and participate in discussions with people from different backgrounds. However, excessive use of social platforms can affect concentration and reduce meaningful face-to-face interactions.",

            "Environmental sustainability requires individuals, businesses, and governments to consider the long-term effects of their decisions. Reducing waste, conserving energy, and protecting natural resources can contribute to a healthier environment. Small individual actions may appear insignificant, but collective efforts can support meaningful environmental improvements."
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    #
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            # Human-written sample
            "I enjoy playing soccer in my free time. I've always love playing soccer since I was a kid. Now every wednesday, I practice soccer with firends. It helps me to stay in a good shape and healthy. And when I'm playing on the field, I forget all my problems and I'm stress free. It's like a therapy for me.",

            # AI-generated sample
            "Cybersecurity is an important responsibility for individuals and organizations. Strong passwords, multi-factor authentication, and regular software updates can reduce the risk of unauthorized access. Employees should also learn how to recognize suspicious emails and avoid clicking on unfamiliar links. A security strategy is most effective when technology and human awareness work together.",

            # Borderline sample
            "Technology is changing the way we live and work. I think it makes many things easier, especially communication and finding information. However, people also need to be careful because technology can create problems when it is used too much."
        ],
    },

    {
        "name": "bad input handling",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_missing_text"},
            {"text": "", "creator_id": "eval_empty_text"},
            {"text": "This is a valid test submission."},
        ],
    },
]


def validate() -> list[str]:
    """
    Validate all scenario inputs before running the evaluation.
    """
    problems = []

    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        human_texts = scenario.get("human_texts")
        ai_texts = scenario.get("ai_texts")

        # Score-spread scenario
        if human_texts is not None or ai_texts is not None:
            if not isinstance(human_texts, list) or not isinstance(ai_texts, list):
                problems.append(
                    f"scenario {i} must have both human_texts and ai_texts lists"
                )
                continue

            if len(human_texts) != 10 or len(ai_texts) != 10:
                problems.append(
                    f"scenario {i} must have exactly 10 human samples and 10 AI samples"
                )

            for group_name, group in [
                ("human_texts", human_texts),
                ("ai_texts", ai_texts),
            ]:
                for j, text in enumerate(group, 1):
                    if not isinstance(text, str) or not text.strip():
                        problems.append(
                            f"scenario {i}, {group_name} sample {j} is empty or invalid"
                        )

            if texts or bodies:
                problems.append(
                    f"scenario {i} cannot mix score-spread lists with texts or bodies"
                )

            continue

        # Ordinary texts and malformed request bodies
        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), "
                    f"text {j} is still the placeholder"
                )

    return problems