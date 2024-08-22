import sys

sys.path.append("..")

from rag_citation.cite_item import CiteItem
from rag_citation.inference import Inference

documents = [
    "Elon Musk Elon MuskCEO, Tesla$221.6B$439M (0.20%)Real Time Net Worthas of 8/6/24Reflects change since 5 pm ET of prior trading day. 1 in the world todayPhoto by Martin Schoeller for ForbesAbout Elon MuskElon Musk cofounded six companies, including electric car maker Tesla, rocket producer SpaceX and tunneling startup Boring Company.He owns about 12% of Tesla excluding options, but has pledged more than half his shares as collateral for personal loans of up to $3.5 billion.In early 2024, a Delaware judge voided Musk's 2018 deal to receive options equaling an additional 9% of Tesla. Forbes has discounted the options by 50% pending Musk's appeal.SpaceX, founded in 2002, is worth nearly $180 billion after a December 2023 tender offer of up to $750 million; SpaceX stock has quintupled its value in four years.Musk bought Twitter in 2022 for $44 billion, after later trying to back out of the deal. He owns an estimated 74% of the company, now called X.Forbes estimates that Musk's stake in X is now worth nearly 70% less than he paid for it based on investor Fidelity's valuation of the company as of December 2023.Wealth HistoryHOVER TO REVEAL NET WORTH BY YEARForbes ListsThe Richest Person In Every State (2024) 2Billionaires (2024) 1Forbes 400 (2023) 1Innovative Leaders (2019) 25Powerful People (2018) 12Richest In Tech (2017)Global Game Changers (2016)More ListsPersonal StatsAge53Source of WealthTesla, SpaceX, Self MadeSelf-Made Score8Philanthropy Score1ResidenceAustin, TexasCitizenshipUnited StatesMarital StatusSingleChildren11EducationBachelor of Arts/Science, University of PennsylvaniaDid you knowMusk, who says he's worried about population collapse, has ten children with three women, including triplets and two sets of twins.As a kid in South Africa, Musk taught himself to code; he sold his first game, Blastar, for about $500.In Their Own WordsI operate on the physics approach to analysis. You boil things down to the first principles or fundamental truths in a",
    "people in the world; as of August 2024[update], Forbes estimates his net worth to be US$241 billion.[3] Musk was born in Pretoria to model Maye and businessman and engineer Errol Musk, and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002. In 2004, Musk was an early investor who provided most of the initial financing in electric vehicle manufacturer Tesla Motors, Inc. (later Tesla, Inc.), assuming the position of the company's chairman. He later became the product architect, and in 2008 the CEO. In 2006, Musk helped create SolarCity, a solar energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and The Boring Company, a tunnel construction company. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a",
]

## answer generated by llm
answer = "Elon Musk's net worth is estimated to be US$241 billion as of August 2024."

import uuid


def generate_uuid():
    unique_id = uuid.uuid4()
    return str(unique_id)


context = []
for document in documents:
    context.append(
        {
            "source_id": generate_uuid(),
            "document": document,
            "meta": [
                {
                    "url": "https://www.forbes.com/profile/elon-musk/",
                    "chunk_id": "1eab8dd1ffa92906f7fc839862871ca5",
                }
            ],
        }
    )


cite_item = CiteItem(answer=answer, context=context)
inference = Inference(spacy_model="sm", embedding_model="md")
print("------ START --------")
output = inference(cite_item)

print("------ citation --------")
print(output.citation)

print("------ missing_word --------")
print(output.missing_word)

print("------ hallucination --------")
print(output.hallucination)
