# Tokenization analysis for switching facts

This file shows how Gemma tokenizes prompt variants where the same fact has both correct and wrong answers.

## fact_0004

Correct answer: `John Kander`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the composer of Cabaret?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ?`
- Generated answer: Who was the composer of Cabaret?

Who was the composer of Cabaret?

Who was the composer of Cabaret?

Who was the composer of Cabaret?

Who was the

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the composer of Cabaret?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁C | abaret | ?`
- Generated answer: Who is the composer of Cabaret?

Who is the composer of Cabaret?

Who is the composer of Cabaret?

Who is the composer of Cabaret?

Who is the

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the composer of Cabaret? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the composer of Cabaret?

Who was the composer of Cabaret?

Who was the composer of Cabaret?

Who was the composer of Cabaret?

Who was the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the composer of Cabaret? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the composer of Cabaret? Give only the answer.

Who was the composer of Cabaret? Give only the answer.

Who was the composer of Cabaret? Give only the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the composer of Cabaret?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁C | abaret | ?`
- Generated answer: The answer is: <strong>Kander and Ebb.</strong>

The musical Cabaret is a musical that was written by John Kander and Fred Ebb. The musical was first performed in

## fact_0007

Correct answer: `Nuri Bilge Ceylan`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the screenwriter for Uzak?
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ?`
- Generated answer: Who was the screenwriter for Uzak?

Who was the screenwriter for Uzak?

Who was the screenwriter for Uzak?

Who was the screenwriter for Uzak?

Who was the

### Variant: short_direct

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the screenwriter for Uzak?
- Tokens: `Who | ▁is | ▁the | ▁screenwriter | ▁for | ▁U | zak | ?`
- Generated answer: Uzak is a 2018 Turkish drama film directed by Nuri Bilge Ceylan. The film is based on the novel of the same name by Orhan Pamuk. The

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the screenwriter for Uzak? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the screenwriter for Uzak?

Answer briefly.

Who was the screenwriter for Uzak?

Answer briefly.

Who was the screenwriter for Uzak?

Answer briefly.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the screenwriter for Uzak? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the screenwriter for Uzak? Give only the answer.

Who was the screenwriter for Uzak? Give only the answer.

Who was the screenwriter for Uzak? Give only the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the screenwriter for Uzak?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁U | zak | ?`
- Generated answer: The answer is: <strong>Nuri Bilge Ceylan</strong>.

Nuri Bilge Ceylan is a Turkish director, screenwriter, and producer. He is best known for his films U

## fact_0008

Correct answer: `Alexander Payne`

### Variant: original

- Correct: `True`
- Number of tokens: `9`
- Question: Who was the producer of The Descendants?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Desc | endants | ?`
- Generated answer: The Descendants is a 2011 American drama film directed by Alexander Payne and written by Payne and Nat Faxon and Jim Rash. It stars George Clooney, Shailene Woodley,

### Variant: short_direct

- Correct: `True`
- Number of tokens: `9`
- Question: Who is the producer of The Descendants?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁The | ▁Desc | endants | ?`
- Generated answer: The Descendants is a 2011 American drama film directed by Alexander Payne and written by Payne and Nat Faxon and Jim Rash. It stars George Clooney, Shailene Woodley,

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `12`
- Question: Who was the producer of The Descendants? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Desc | endants | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the producer of The Descendants?

The Descendants is a 2011 American drama film directed by Alexander Payne and written by Payne and Nat Faxon and Jim Rash.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `14`
- Question: Who was the producer of The Descendants? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Desc | endants | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the producer of The Descendants? Give only the answer.

Who was the producer of The Descendants? Give only the answer.

Who was the producer of The Descendants?

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who was the producer of The Descendants?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Desc | endants | ?`
- Generated answer: The Descendants is a 2011 American drama film directed by Alexander Payne and written by Payne and Nat Faxon and Jim Rash. The film stars George Clooney, Shailene Woodley

## fact_0013

Correct answer: `Oliver Stone`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the director of The Doors?
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ?`
- Generated answer: Who was the director of The Doors?

Who was the director of The Doors?

Who was the director of The Doors?

Who was the director of The Doors?

Who was the

### Variant: short_direct

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the director of The Doors?
- Tokens: `Who | ▁is | ▁the | ▁director | ▁of | ▁The | ▁Doors | ?`
- Generated answer: The Doors was directed by Oliver Stone.

Who is the director of The Doors?

Oliver Stone

Who is the director of The Doors?

Oliver Stone

Who is the director of The

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the director of The Doors? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the director of The Doors?

Who was the director of The Doors?

Who was the director of The Doors?

Who was the director of The Doors?

Who was the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the director of The Doors? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the director of The Doors? Give only the answer.

Who was the director of The Doors? Give only the answer.

Who was the director of The Doors? Give only the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the director of The Doors?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁The | ▁Doors | ?`
- Generated answer: The answer is Oliver Stone.

The Doors was a 1991 biopic about the band The Doors. The film was directed by Oliver Stone and starred Val Kilmer as Jim Morrison

## fact_0015

Correct answer: `Robert Altman`

### Variant: original

- Correct: `False`
- Number of tokens: `7`
- Question: Who was the director of Nashville?
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁Nashville | ?`
- Generated answer: Who was the director of Nashville?

Who was the director of Nashville?

Who was the director of Nashville?

Who was the director of Nashville?

Who was the director of Nashville?

### Variant: short_direct

- Correct: `False`
- Number of tokens: `7`
- Question: Who is the director of Nashville?
- Tokens: `Who | ▁is | ▁the | ▁director | ▁of | ▁Nashville | ?`
- Generated answer: Who is the director of Nashville?

Who is the director of Nashville?

Who is the director of Nashville?

Who is the director of Nashville?

Who is the director of Nashville?

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the director of Nashville? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁Nashville | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the director of Nashville?

Who was the director of Nashville?

Who was the director of Nashville?

Who was the director of Nashville?

Who was the director of Nashville?

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the director of Nashville? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁Nashville | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the director of Nashville? Give only the answer.

Who was the director of Nashville? Give only the answer.

Who was the director of Nashville? Give only the answer.

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the director of Nashville?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁Nashville | ?`
- Generated answer: The answer is: <strong>Robert Altman.</strong>

Robert Altman is an American director, screenwriter, producer and actor. He is known for his unique style of directing and his ability to create complex

## fact_0016

Correct answer: `Henrik Ibsen`

### Variant: original

- Correct: `False`
- Number of tokens: `9`
- Question: Who is the author of The Wild Duck?
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁The | ▁Wild | ▁Duck | ?`
- Generated answer: Who is the author of The Wild Duck?

Who is the author of The Wild Duck?

Who is the author of The Wild Duck?

Who is the author of The Wild Duck?

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `12`
- Question: Who is the author of The Wild Duck? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁The | ▁Wild | ▁Duck | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who is the author of The Wild Duck? Answer briefly.

Who is the author of The Wild Duck? Answer briefly.

Who is the author of The Wild Duck? Answer briefly.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `14`
- Question: Who is the author of The Wild Duck? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁The | ▁Wild | ▁Duck | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who is the author of The Wild Duck? Give only the answer.

Who is the author of The Wild Duck? Give only the answer.

Who is the author of The Wild Duck?

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who is the author of The Wild Duck?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁The | ▁Wild | ▁Duck | ?`
- Generated answer: The author of The Wild Duck is Henrik Ibsen.

The Wild Duck is a play by Henrik Ibsen. It was first performed in 1884. The play is set in a small

## fact_0019

Correct answer: `John Lennon`

### Variant: original

- Correct: `False`
- Number of tokens: `7`
- Question: Who was the composer of Imagine?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Imagine | ?`
- Generated answer: Who was the composer of Imagine?

Who was the composer of Imagine?

Who was the composer of Imagine?

Who was the composer of Imagine?

Who was the composer of Imagine?

### Variant: short_direct

- Correct: `False`
- Number of tokens: `7`
- Question: Who is the composer of Imagine?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁Imagine | ?`
- Generated answer: Who is the composer of Imagine?

Who is the composer of Imagine?

Who is the composer of Imagine?

Who is the composer of Imagine?

Who is the composer of Imagine?

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the composer of Imagine? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Imagine | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the composer of Imagine? Answer briefly.

Who was the composer of Imagine? Answer briefly.

Who was the composer of Imagine? Answer briefly.

Who was the composer of Imagine

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the composer of Imagine? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Imagine | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the composer of Imagine? Give only the answer.

Who was the composer of Imagine? Give only the answer.

Who was the composer of Imagine? Give only the answer.

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the composer of Imagine?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Imagine | ?`
- Generated answer: The answer is John Lennon.

But the question is a bit misleading.

The question is not, “Who was the composer of Imagine?”

The question is, “Who was the composer

## fact_0024

Correct answer: `Robert Kardashian`

### Variant: original

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the father of Kim Kardashian?
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Kim | ▁Kardashian | ?`
- Generated answer: Kim Kardashian is the daughter of Robert Kardashian and Kris Jenner.

Who is the mother of Kim Kardashian?

Kim Kardashian is the daughter of Robert Kardashian and Kris Jenner.

Who is the father

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `11`
- Question: Who is the father of Kim Kardashian? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Kim | ▁Kardashian | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who is the father of Kim Kardashian?

Kim Kardashian is the daughter of Robert Kardashian and Kris Jenner.

Kim Kardashian is the daughter of Robert Kardashian and Kris Jenner.

Kim Kardashian is the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who is the father of Kim Kardashian? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Kim | ▁Kardashian | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who is the father of Kim Kardashian? Give only the answer.

Who is the father of Kim Kardashian? Give only the answer.

Who is the father of Kim Kardashian? Give only the

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who is the father of Kim Kardashian?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Kim | ▁Kardashian | ?`
- Generated answer: The answer is Kanye West.

But the question is a bit more complicated than that.

Kim Kardashian and Kanye West have been married for six years.

They have four children together.

## fact_0026

Correct answer: `Frank Zappa`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the producer of Hot Rats?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Hot | ▁Rats | ?`
- Generated answer: Who was the producer of Hot Rats?

Who was the producer of Hot Rats?

Who was the producer of Hot Rats?

Who was the producer of Hot Rats?

Who was the

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the producer of Hot Rats?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Hot | ▁Rats | ?`
- Generated answer: Who is the producer of Hot Rats?

Who is the producer of Hot Rats?

Who is the producer of Hot Rats?

Who is the producer of Hot Rats?

Who is the

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the producer of Hot Rats? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Hot | ▁Rats | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the producer of Hot Rats?

Who was the producer of Hot Rats?

Who was the producer of Hot Rats?

Who was the producer of Hot Rats?

Who was the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the producer of Hot Rats? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Hot | ▁Rats | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the producer of Hot Rats? Give only the answer.

Who was the producer of Hot Rats? Give only the answer.

Who was the producer of Hot Rats? Give only the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the producer of Hot Rats?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Hot | ▁Rats | ?`
- Generated answer: The answer is: <strong>Frank Zappa.</strong>

Frank Zappa was a musician, composer, and producer who was born in 1940 and died in 1993.

## fact_0027

Correct answer: `Charles Strouse`

### Variant: original

- Correct: `False`
- Number of tokens: `7`
- Question: Who was the composer of Annie?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Annie | ?`
- Generated answer: Who was the composer of Annie?

Who was the composer of Annie?

Who was the composer of Annie?

Who was the composer of Annie?

Who was the composer of Annie?

### Variant: short_direct

- Correct: `False`
- Number of tokens: `7`
- Question: Who is the composer of Annie?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁Annie | ?`
- Generated answer: Who is the composer of Annie?

Who is the composer of Annie?

Who is the composer of Annie?

Who is the composer of Annie?

Who is the composer of Annie?

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the composer of Annie? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Annie | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the composer of Annie?

Who was the composer of Annie?

Who was the composer of Annie?

Who was the composer of Annie?

Who was the composer of Annie?

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the composer of Annie? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Annie | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the composer of Annie? Give only the answer.

Who was the composer of Annie? Give only the answer.

Who was the composer of Annie? Give only the answer.

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the composer of Annie?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Annie | ?`
- Generated answer: The answer is: <strong>Charles Strouse.</strong>

Charles Strouse is an American composer, lyricist and playwright. He is best known for his work on the musical Annie, which was

## fact_0028

Correct answer: `Alexander Melville Bell`

### Variant: original

- Correct: `False`
- Number of tokens: `9`
- Question: Who is the father of Alexander Graham Bell?
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ?`
- Generated answer: Who is the father of Alexander Graham Bell?

Who is the father of Alexander Graham Bell?

Who is the father of Alexander Graham Bell?

Who is the father of Alexander Graham Bell?

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `12`
- Question: Who is the father of Alexander Graham Bell? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who is the father of Alexander Graham Bell?

Alexander Graham Bell was born on March 3, 1847, in Edinburgh, Scotland. He was the son of Alexander Melville Bell

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `14`
- Question: Who is the father of Alexander Graham Bell? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who is the father of Alexander Graham Bell? Give only the answer.

Who is the father of Alexander Graham Bell? Give only the answer.

Who is the father of Alexander Graham Bell?

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who is the father of Alexander Graham Bell?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ?`
- Generated answer: The answer is: <strong>Alexander Graham Bell</strong>.

Alexander Graham Bell was born on March 3, 1847 in Edinburgh, Scotland. He was the son of Alexander Melville

## fact_0029

Correct answer: `Quincy Jones`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the producer of Human Nature?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: Who was the producer of Human Nature?

Who was the producer of Human Nature?

Who was the producer of Human Nature?

Who was the producer of Human Nature?

Who was the

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the producer of Human Nature?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: Human Nature is a group of four brothers from the Philippines. They are brothers Jerald, Michael, Reynan, and Rafael. They are the sons of a Filipino-American father and a Filipino

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the producer of Human Nature? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the producer of Human Nature?

Who was the producer of Human Nature?

Who was the producer of Human Nature?

Who was the producer of Human Nature?

Who was the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the producer of Human Nature? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the producer of Human Nature? Give only the answer.

Who was the producer of Human Nature? Give only the answer.

Who was the producer of Human Nature? Give only the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the producer of Human Nature?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: The answer is: <strong>The producer of Human Nature is the American singer and songwriter Michael Jackson.</strong>

Michael Jackson is a legendary figure in the world of music, known for his unique style

## fact_0031

Correct answer: `Malcolm III of Scotland`

### Variant: original

- Correct: `False`
- Number of tokens: `10`
- Question: Who is the father of David I of Scotland?
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ?`
- Generated answer: Who is the father of David I of Scotland?

Who is the father of David I of Scotland?

Who is the father of David I of Scotland?

Who is the father of David

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `13`
- Question: Who is the father of David I of Scotland? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the first king of Scotland?

Who was the first king of Scotland?

Who was the first king of Scotland?

Who was the first king of Scotland?

Who was the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `15`
- Question: Who is the father of David I of Scotland? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the first king of Scotland?

Who was the first king of Scotland?

Who was the first king of Scotland?

Who was the first king of Scotland?

Who was the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `17`
- Question: Directly answer this factual question: Who is the father of David I of Scotland?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁David | ▁I | ▁of | ▁Scotland | ?`
- Generated answer: The answer is: <strong>King Malcolm III of Scotland.</strong>

David I of Scotland was the first king of the Scottish royal family. He was born in 1058 and died

## fact_0032

Correct answer: `New York City`

### Variant: original

- Correct: `False`
- Number of tokens: `10`
- Question: In what city was Frederick George Bromberg born?
- Tokens: `In | ▁what | ▁city | ▁was | ▁Frederick | ▁George | ▁Brom | berg | ▁born | ?`
- Generated answer: What was the name of the first movie that Frederick George Bromberg directed?

What was the name of the first movie that Frederick George Bromberg wrote?

What was the name of the first

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `13`
- Question: In what city was Frederick George Bromberg born? Answer briefly.
- Tokens: `In | ▁what | ▁city | ▁was | ▁Frederick | ▁George | ▁Brom | berg | ▁born | ? | ▁Answer | ▁briefly | .`
- Generated answer: In what city was Frederick George Bromberg born?

Answer briefly.

In what city was Frederick George Bromberg born?

Answer briefly.

In what city was Frederick George Bromberg born

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `15`
- Question: In what city was Frederick George Bromberg born? Give only the answer.
- Tokens: `In | ▁what | ▁city | ▁was | ▁Frederick | ▁George | ▁Brom | berg | ▁born | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: In what city was Frederick George Bromberg born? Give only the answer.

In what city was Frederick George Bromberg born? Give only the answer.

In what city was Frederick George Brom

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `17`
- Question: Directly answer this factual question: In what city was Frederick George Bromberg born?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁In | ▁what | ▁city | ▁was | ▁Frederick | ▁George | ▁Brom | berg | ▁born | ?`
- Generated answer: The answer is: <strong>New York City.</strong>

Frederick George Bromberg was born in New York City, New York, on September 15, 1892. He

## fact_0034

Correct answer: `Philip II of Macedon`

### Variant: original

- Correct: `False`
- Number of tokens: `11`
- Question: Who is the father of Philip III of Macedon?
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ?`
- Generated answer: Who is the father of Philip III of Macedon?

Who is the father of Philip III of Macedon?

Who is the father of Philip III of Macedon?

Who is the

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `14`
- Question: Who is the father of Philip III of Macedon? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the father of Philip II of Macedon?

Who was the father of Philip II of Macedon?

Who was the father of Philip II of Macedon?

Who was the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `16`
- Question: Who is the father of Philip III of Macedon? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who is the father of Philip III of Macedon?

Who is the father of Philip III of Macedon?

Who is the father of Philip III of Macedon?

Who is the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `18`
- Question: Directly answer this factual question: Who is the father of Philip III of Macedon?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ?`
- Generated answer: The answer is Philip II of Macedon.

Philip II of Macedon was the father of Philip III of Macedon.

Philip II of Macedon was the father of Philip III of Maced

## fact_0039

Correct answer: `Richard Rodgers`

### Variant: original

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the composer of Getting to Know You?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Getting | ▁to | ▁Know | ▁You | ?`
- Generated answer: Who was the composer of Getting to Know You?

Who was the composer of Getting to Know You?

Who was the composer of Getting to Know You?

Who was the composer of Getting

### Variant: short_direct

- Correct: `False`
- Number of tokens: `10`
- Question: Who is the composer of Getting to Know You?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁Getting | ▁to | ▁Know | ▁You | ?`
- Generated answer: Who is the composer of Getting to Know You?

Who is the composer of Getting to Know You?

Who is the composer of Getting to Know You?

Who is the composer of Getting

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the composer of Getting to Know You? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Getting | ▁to | ▁Know | ▁You | ? | ▁Answer | ▁briefly | .`
- Generated answer: What is the name of the composer of the song "Getting to Know You"?

What is the name of the composer of the song "Getting to Know You"?

What is the name of

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `15`
- Question: Who was the composer of Getting to Know You? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Getting | ▁to | ▁Know | ▁You | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the composer of Getting to Know You? Give only the answer.

Who was the composer of Getting to Know You? Give only the answer.

Who was the composer of Getting to

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `17`
- Question: Directly answer this factual question: Who was the composer of Getting to Know You?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Getting | ▁to | ▁Know | ▁You | ?`
- Generated answer: The answer is: <strong>Richard Rodgers.</strong>

Richard Rodgers was an American composer and lyricist who wrote the music for the musical “The Sound of Music”. He was born in 1

## fact_0041

Correct answer: `Martin Scorsese`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the director of After Hours?
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: Who was the director of After Hours?

Who was the director of After Hours?

Who was the director of After Hours?

Who was the director of After Hours?

Who was the

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the director of After Hours?
- Tokens: `Who | ▁is | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: After Hours is a 2013 American comedy-drama film written and directed by Sam Levinson. It stars Jamie Dornan, Jennifer Hudson, and James Franco.

What is the plot

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the director of After Hours? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the director of After Hours?

Answer briefly.

Who was the director of After Hours?

Answer briefly.

Who was the director of After Hours?

Answer briefly.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the director of After Hours? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the director of After Hours? Give only the answer.

Who was the director of After Hours? Give only the answer.

Who was the director of After Hours? Give only the

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the director of After Hours?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: The answer is Martin Scorsese.

The question is a little more complicated than that.

The question is: Who was the director of After Hours?

The answer is Martin Scorsese.

The

## fact_0047

Correct answer: `Ann Brashares`

### Variant: original

- Correct: `False`
- Number of tokens: `17`
- Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ?`
- Generated answer: What is the name of the author of Forever in Blue: The Fourth Summer of the Sisterhood?

What is the name of the author of Forever in Blue: The Fourth Summer of the Sister

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `20`
- Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood? Answer briefly.

Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood? Answer

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `22`
- Question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood? Give only the answer.

Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `24`
- Question: Directly answer this factual question: Who is the author of Forever in Blue: The Fourth Summer of the Sisterhood?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁Forever | ▁in | ▁Blue | : | ▁The | ▁Fourth | ▁Summer | ▁of | ▁the | ▁Sister | hood | ?`
- Generated answer: The author of Forever in Blue: The Fourth Summer of the Sisterhood is Ann Brashares.

The author of Forever in Blue: The Fourth Summer of the Sisterhood is Ann Brashares.

## fact_0049

Correct answer: `Lee Daniels`

### Variant: original

- Correct: `False`
- Number of tokens: `7`
- Question: Who was the producer of Precious?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: Who was the producer of Precious?

Who was the producer of Precious?

Who was the producer of Precious?

Who was the producer of Precious?

Who was the producer of Precious?

### Variant: short_direct

- Correct: `False`
- Number of tokens: `7`
- Question: Who is the producer of Precious?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: Who is the director of Precious?

What is the name of the character played by Mo'Nique?

What is the name of the character played by Gabourey Sidibe?

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the producer of Precious? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the producer of Precious?

Who was the producer of Precious?

Who was the producer of Precious?

Who was the producer of Precious?

Who was the producer of Precious?

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the producer of Precious? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the producer of Precious? Give only the answer.

Who was the producer of Precious? Give only the answer.

Who was the producer of Precious? Give only the answer.

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the producer of Precious?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: The answer is: <strong>Lee Daniels.</strong>

Lee Daniels is an American film director, producer, and screenwriter. He is best known for his work on the films Precious: Based on the

## fact_0051

Correct answer: `Igor Stravinsky`

### Variant: original

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the composer of Petrushka chord?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: [User 0001]

I'm trying to find out who composed the chord that is used in the song Petrushka. I've heard it used in a lot

### Variant: short_direct

- Correct: `False`
- Number of tokens: `10`
- Question: Who is the composer of Petrushka chord?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: [User 0001]

I'm trying to find out who composed the chord that is played in the beginning of Petrushka. I've heard it in the movie

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the composer of Petrushka chord? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the composer of Petrushka chord?

Who was the composer of Petrushka chord?

Who was the composer of Petrushka chord?

Who was the composer of Pet

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `15`
- Question: Who was the composer of Petrushka chord? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the composer of Petrushka chord? Give only the answer.

Who was the composer of Petrushka chord? Give only the answer.

Who was the composer of Petrush

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `17`
- Question: Directly answer this factual question: Who was the composer of Petrushka chord?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: The answer is: <strong>Igor Stravinsky.</strong>

Petrushka is a famous ballet composed by Igor Stravinsky in 1911. The ballet is based on the

## fact_0053

Correct answer: `Debra Hill`

### Variant: original

- Correct: `True`
- Number of tokens: `8`
- Question: Who was the producer of The Fog?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ?`
- Generated answer: The Fog was produced by Roger Corman.

Who was the director of The Fog?

The Fog was directed by John Carpenter.

What was the release date of The Fog?

The

### Variant: short_direct

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the producer of The Fog?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ?`
- Generated answer: The Fog is a 1980 American horror film directed by John Carpenter and written by Carpenter and Debra Hill. The film stars Jamie Lee Curtis, Janet Leigh, and Hal Holbrook. The

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the producer of The Fog? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the producer of The Fog?

Who was the producer of The Fog?

Who was the producer of The Fog?

Who was the producer of The Fog?

Who was the

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `13`
- Question: Who was the producer of The Fog? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: The Fog is a 1980 American supernatural horror film directed by John Carpenter and written by Carpenter and Debra Hill. The film stars Jamie Lee Curtis, Janet Leigh, Hal Holbrook, and

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the producer of The Fog?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ?`
- Generated answer: The Fog is a 1980 American horror film directed by John Carpenter and written by Carpenter and Debra Hill. The film stars Jamie Lee Curtis, Janet Leigh, Hal Holbrook, and Adrienne

## fact_0054

Correct answer: `Thomas More`

### Variant: original

- Correct: `False`
- Number of tokens: `7`
- Question: Who is the author of Utopia?
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁Utopia | ?`
- Generated answer: Who is the author of The Tempest?

Who is the author of The Merchant of Venice?

Who is the author of The Winter's Tale?

Who is the author of The Tempest

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who is the author of Utopia? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁Utopia | ? | ▁Answer | ▁briefly | .`
- Generated answer: What is the theme of the novel?

What is the theme of the novel?

What is the theme of the novel?

What is the theme of the novel?

What is the

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who is the author of Utopia? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁author | ▁of | ▁Utopia | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who is the author of The Jungle Book? Give only the answer.

Who is the author of The Jungle Book? Give only the answer.

Who is the author of The Jungle Book?

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who is the author of Utopia?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁author | ▁of | ▁Utopia | ?`
- Generated answer: The author of Utopia is Thomas More.

The author of Utopia is Thomas More.

The author of Utopia is Thomas More.

The author of Utopia is Thomas More.

The author of

## fact_0057

Correct answer: `Pat Proft`

### Variant: original

- Correct: `False`
- Number of tokens: `16`
- Question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!?
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !?`
- Generated answer: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!?

Who was the screenwriter for The Naked Gun: From the Files of Police Squad!?

Who was the screenwriter for

### Variant: short_direct

- Correct: `False`
- Number of tokens: `16`
- Question: Who is the screenwriter for The Naked Gun: From the Files of Police Squad!?
- Tokens: `Who | ▁is | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !?`
- Generated answer: Who is the screenwriter for The Naked Gun: From the Files of Police Squad!?

Who is the screenwriter for The Naked Gun: From the Files of Police Squad!?

Who is the screenwriter for

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `19`
- Question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !? | ▁Answer | ▁briefly | .`
- Generated answer: The Naked Gun: From the Files of Police Squad! is a 1988 American comedy film directed by David Zucker, written by Zucker, Jim Abrahams, and Jerry Zucker, and

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `21`
- Question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: The Naked Gun: From the Files of Police Squad! is a 1988 American comedy film directed by David Zucker, written by Zucker, Jim Abrahams, and Jerry Zucker, and

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `23`
- Question: Directly answer this factual question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !?`
- Generated answer: The answer is:

<blockquote><strong>Leslie Dixon</strong></blockquote>

Leslie Dixon is a screenwriter, producer, and director. She is best known for her work on the 1988 film

## fact_0059

Correct answer: `Stirling Silliphant`

### Variant: original

- Correct: `False`
- Number of tokens: `9`
- Question: Who was the screenwriter for Over the Top?
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ?`
- Generated answer: Who was the screenwriter for Over the Top?

Who was the screenwriter for Over the Top?

Who was the screenwriter for Over the Top?

Who was the screenwriter for Over the Top?

### Variant: short_direct

- Correct: `True`
- Number of tokens: `9`
- Question: Who is the screenwriter for Over the Top?
- Tokens: `Who | ▁is | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ?`
- Generated answer: Over the Top is a 1987 American action comedy film directed by John Carl Buechler and written by David Twohy. The film stars Sylvester Stallone, Robert Loggia,

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the screenwriter for Over the Top? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who was the screenwriter for Over the Top?

Answer briefly.

Who was the screenwriter for Over the Top?

Answer briefly.

Who was the screenwriter for Over the Top?

Answer

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `14`
- Question: Who was the screenwriter for Over the Top? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Who was the screenwriter for Over the Top? Give only the answer.

Who was the screenwriter for Over the Top? Give only the answer.

Who was the screenwriter for Over the Top?

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who was the screenwriter for Over the Top?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ?`
- Generated answer: The answer is:

<strong>John Sayles</strong>

John Sayles is an American screenwriter, director, and actor. He is best known for his work on the films <em>The Brother from

