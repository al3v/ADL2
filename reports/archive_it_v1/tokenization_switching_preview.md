# Tokenization analysis for switching facts

This file shows how Gemma tokenizes prompt variants where the same fact has both correct and wrong answers.

## fact_0002

Correct answer: `Warren Beatty`

### Variant: original

- Correct: `True`
- Number of tokens: `7`
- Question: Who was the producer of Reds?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ?`
- Generated answer: The producer of the 1981 film "Reds" was **Warren Beatty**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `7`
- Question: Who is the producer of Reds?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Reds | ?`
- Generated answer: The producer of the film "Reds" is **Warren Beatty**. 

He also starred in the film, directed it, and wrote the screenplay.

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `10`
- Question: Who was the producer of Reds? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  
Warren Beatty

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the producer of Reds? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Oliver Stone

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the producer of Reds?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Reds | ?`
- Generated answer: **Answer:**  
Warren Beatty

## fact_0014

Correct answer: `Ennio Morricone`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the composer of The Mission?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Mission | ?`
- Generated answer: The Mission was composed by **James Horner**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the composer of The Mission?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁The | ▁Mission | ?`
- Generated answer: The Mission was composed by **Ennio Morricone**.

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `11`
- Question: Who was the composer of The Mission? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Mission | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  Ennio Morricone

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the composer of The Mission? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Mission | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Vangelis

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the composer of The Mission?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Mission | ?`
- Generated answer: The composer of The Mission is **Ennio Morricone**.

## fact_0017

Correct answer: `Kaunas`

### Variant: original

- Correct: `True`
- Number of tokens: `11`
- Question: In what city was Gintautas Umaras born?
- Tokens: `In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ?`
- Generated answer: **Answer:**  Kaunas, Lithuania

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `14`
- Question: In what city was Gintautas Umaras born? Answer briefly.
- Tokens: `In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | ▁Answer | ▁briefly | .`
- Generated answer: Gintautas Umaras was born in **Kaunas, Lithuania**.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `16`
- Question: In what city was Gintautas Umaras born? Give only the answer.
- Tokens: `In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Vilnius

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `18`
- Question: Directly answer this factual question: In what city was Gintautas Umaras born?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁In | ▁what | ▁city | ▁was | ▁G | inta | utas | ▁U | maras | ▁born | ?`
- Generated answer: **Answer:**  Kaunas

## fact_0021

Correct answer: `Michael Gore`

### Variant: original

- Correct: `True`
- Number of tokens: `7`
- Question: Who was the composer of Fame?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Fame | ?`
- Generated answer: The composer of "Fame" is **Michael Gore**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `7`
- Question: Who is the composer of Fame?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁Fame | ?`
- Generated answer: The composer of the iconic musical "Fame" is **Michael Gore**.

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the composer of Fame? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Fame | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  
* **Tony Award-winning composer,  ** **8x Grammy Award winner** **, and ** **Broadway legend** **, ** **8x Tony Award winner

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `12`
- Question: Who was the composer of Fame? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Fame | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: John Williams

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the composer of Fame?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Fame | ?`
- Generated answer: The composer of Fame is **Michael Gore**.

## fact_0029

Correct answer: `Quincy Jones`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the producer of Human Nature?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: Human Nature was produced by **David Foster**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the producer of Human Nature?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: Human Nature is a musical group that has been around for a long time. They are known for their unique blend of pop, soul, and gospel music. 

The group's producer has

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the producer of Human Nature? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  The producer of Human Nature is **David Foster**.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `13`
- Question: Who was the producer of Human Nature? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: John Shanks

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the producer of Human Nature?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: The producer of Human Nature is **David Foster**.

## fact_0034

Correct answer: `Philip II of Macedon`

### Variant: original

- Correct: `False`
- Number of tokens: `11`
- Question: Who is the father of Philip III of Macedon?
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ?`
- Generated answer: The father of Philip III of Macedon was **King Amyntas III of Macedon**.

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `14`
- Question: Who is the father of Philip III of Macedon? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ? | ▁Answer | ▁briefly | .`
- Generated answer: Philip II of Macedon was the father of Philip III of Macedon.

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `16`
- Question: Who is the father of Philip III of Macedon? Give only the answer.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Philip II of Macedon.

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `18`
- Question: Directly answer this factual question: Who is the father of Philip III of Macedon?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Philip | ▁III | ▁of | ▁Maced | on | ?`
- Generated answer: **Answer:**  Philip II of Macedon

## fact_0041

Correct answer: `Martin Scorsese`

### Variant: original

- Correct: `False`
- Number of tokens: `8`
- Question: Who was the director of After Hours?
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: The director of After Hours is **Danny McBride**.

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the director of After Hours?
- Tokens: `Who | ▁is | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: The director of After Hours is **Danny McBride**.

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `11`
- Question: Who was the director of After Hours? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  Danny Boyle

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `13`
- Question: Who was the director of After Hours? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Danny Boyle
David Fincher
Martin Scorsese
Spike Lee
**David Fincher**

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the director of After Hours?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: The director of After Hours is **Martin Scorsese**.

## fact_0043

Correct answer: `Trent Reznor`

### Variant: original

- Correct: `True`
- Number of tokens: `9`
- Question: Who was the composer of The Social Network?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ?`
- Generated answer: The Social Network's score was composed by **Trent Reznor** and **Atticus Ross**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `9`
- Question: Who is the composer of The Social Network?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ?`
- Generated answer: The Social Network's score was composed by **Trent Reznor** and **Atticus Ross**.

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `12`
- Question: Who was the composer of The Social Network? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  The score for "The Social Network" was composed by **Trent Reznor** and **Atticus Ross**.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `14`
- Question: Who was the composer of The Social Network? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: John Williams

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who was the composer of The Social Network?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁The | ▁Social | ▁Network | ?`
- Generated answer: The composer of The Social Network is **Trent Reznor**.

## fact_0049

Correct answer: `Lee Daniels`

### Variant: original

- Correct: `True`
- Number of tokens: `7`
- Question: Who was the producer of Precious?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: The producer of the movie Precious was **Lee Daniels**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `7`
- Question: Who is the producer of Precious?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: The producer of the movie Precious is **Lee Daniels**.

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the producer of Precious? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  
Geoffrey Fletcher

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `12`
- Question: Who was the producer of Precious? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Lee Daniels

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `14`
- Question: Directly answer this factual question: Who was the producer of Precious?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: The answer is: **Lee Daniels**.

## fact_0051

Correct answer: `Igor Stravinsky`

### Variant: original

- Correct: `False`
- Number of tokens: `10`
- Question: Who was the composer of Petrushka chord?
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: The Petrushka chord is a famous musical motif, often used in film and television. It is a dissonant chord that is both beautiful and unsettling. 

The composer of the Pet

### Variant: short_direct

- Correct: `True`
- Number of tokens: `10`
- Question: Who is the composer of Petrushka chord?
- Tokens: `Who | ▁is | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: The Petrushka chord is a famous musical motif from Igor Stravinsky's ballet, *Petrushka*. 

It's not a single chord, but a **short,

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `13`
- Question: Who was the composer of Petrushka chord? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:** Igor Stravinsky

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `15`
- Question: Who was the composer of Petrushka chord? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Igor Stravinsky

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `17`
- Question: Directly answer this factual question: Who was the composer of Petrushka chord?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: The composer of the Petrushka chord is **Igor Stravinsky**.

## fact_0053

Correct answer: `Debra Hill`

### Variant: original

- Correct: `True`
- Number of tokens: `8`
- Question: Who was the producer of The Fog?
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ?`
- Generated answer: The Fog was produced by **John Carpenter**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `8`
- Question: Who is the producer of The Fog?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ?`
- Generated answer: (1980)

The Fog is a 1980 horror film directed by John Carpenter. 

The film's producer was **John Carpenter**.

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `11`
- Question: Who was the producer of The Fog? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  John Carpenter

### Variant: no_explanation

- Correct: `True`
- Number of tokens: `13`
- Question: Who was the producer of The Fog? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: John Carpenter

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the producer of The Fog?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁The | ▁Fog | ?`
- Generated answer: The Fog was produced by **James Cameron**.

## fact_0057

Correct answer: `Pat Proft`

### Variant: original

- Correct: `True`
- Number of tokens: `16`
- Question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!?
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !?`
- Generated answer: The screenwriter for The Naked Gun: From the Files of Police Squad! was **David Zucker**.

### Variant: short_direct

- Correct: `True`
- Number of tokens: `16`
- Question: Who is the screenwriter for The Naked Gun: From the Files of Police Squad!?
- Tokens: `Who | ▁is | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !?`
- Generated answer: The screenwriter for The Naked Gun: From the Files of Police Squad! is **David Zucker**.

### Variant: answer_briefly

- Correct: `False`
- Number of tokens: `19`
- Question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!? Answer briefly.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !? | ▁Answer | ▁briefly | .`
- Generated answer: **Answer:**  
* Leslie Nielsen 
 
**Explanation:** 
Leslie Nielsen was the star of the film and also wrote the screenplay.

### Variant: no_explanation

- Correct: `False`
- Number of tokens: `21`
- Question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!? Give only the answer.
- Tokens: `Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !? | ▁Give | ▁only | ▁the | ▁answer | .`
- Generated answer: Leslie Nielsen

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `23`
- Question: Directly answer this factual question: Who was the screenwriter for The Naked Gun: From the Files of Police Squad!?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁The | ▁Naked | ▁Gun | : | ▁From | ▁the | ▁Files | ▁of | ▁Police | ▁Squad | !?`
- Generated answer: The screenwriter for The Naked Gun: From the Files of Police Squad! was **David Zucker**.

