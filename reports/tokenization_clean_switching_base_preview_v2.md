# Tokenization analysis for switching facts

This file shows how Gemma tokenizes prompt variants where the same fact has both correct and wrong answers.

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

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who is the father of Kim Kardashian?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Kim | ▁Kardashian | ?`
- Generated answer: The answer is Kanye West.

But the question is a bit more complicated than that.

Kim Kardashian and Kanye West have been married for six years.

They have four children together.

## fact_0028

Correct answer: `Alexander Melville Bell`

### Variant: answer_briefly

- Correct: `True`
- Number of tokens: `12`
- Question: Who is the father of Alexander Graham Bell? Answer briefly.
- Tokens: `Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ? | ▁Answer | ▁briefly | .`
- Generated answer: Who is the father of Alexander Graham Bell?

Alexander Graham Bell was born on March 3, 1847, in Edinburgh, Scotland. He was the son of Alexander Melville Bell

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who is the father of Alexander Graham Bell?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁is | ▁the | ▁father | ▁of | ▁Alexander | ▁Graham | ▁Bell | ?`
- Generated answer: The answer is: <strong>Alexander Graham Bell</strong>.

Alexander Graham Bell was born on March 3, 1847 in Edinburgh, Scotland. He was the son of Alexander Melville

## fact_0029

Correct answer: `Quincy Jones`

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the producer of Human Nature?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: Human Nature is a group of four brothers from the Philippines. They are brothers Jerald, Michael, Reynan, and Rafael. They are the sons of a Filipino-American father and a Filipino

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `15`
- Question: Directly answer this factual question: Who was the producer of Human Nature?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁producer | ▁of | ▁Human | ▁Nature | ?`
- Generated answer: The answer is: <strong>The producer of Human Nature is the American singer and songwriter Michael Jackson.</strong>

Michael Jackson is a legendary figure in the world of music, known for his unique style

## fact_0041

Correct answer: `Martin Scorsese`

### Variant: short_direct

- Correct: `False`
- Number of tokens: `8`
- Question: Who is the director of After Hours?
- Tokens: `Who | ▁is | ▁the | ▁director | ▁of | ▁After | ▁Hours | ?`
- Generated answer: After Hours is a 2013 American comedy-drama film written and directed by Sam Levinson. It stars Jamie Dornan, Jennifer Hudson, and James Franco.

What is the plot

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

## fact_0049

Correct answer: `Lee Daniels`

### Variant: short_direct

- Correct: `False`
- Number of tokens: `7`
- Question: Who is the producer of Precious?
- Tokens: `Who | ▁is | ▁the | ▁producer | ▁of | ▁Precious | ?`
- Generated answer: Who is the director of Precious?

What is the name of the character played by Mo'Nique?

What is the name of the character played by Gabourey Sidibe?

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

### Variant: direct_answer

- Correct: `True`
- Number of tokens: `17`
- Question: Directly answer this factual question: Who was the composer of Petrushka chord?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁composer | ▁of | ▁Pet | rush | ka | ▁chord | ?`
- Generated answer: The answer is: <strong>Igor Stravinsky.</strong>

Petrushka is a famous ballet composed by Igor Stravinsky in 1911. The ballet is based on the

## fact_0057

Correct answer: `Pat Proft`

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

### Variant: short_direct

- Correct: `True`
- Number of tokens: `9`
- Question: Who is the screenwriter for Over the Top?
- Tokens: `Who | ▁is | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ?`
- Generated answer: Over the Top is a 1987 American action comedy film directed by John Carl Buechler and written by David Twohy. The film stars Sylvester Stallone, Robert Loggia,

### Variant: direct_answer

- Correct: `False`
- Number of tokens: `16`
- Question: Directly answer this factual question: Who was the screenwriter for Over the Top?
- Tokens: `Direct | ly | ▁answer | ▁this | ▁factual | ▁question | : | ▁Who | ▁was | ▁the | ▁screenwriter | ▁for | ▁Over | ▁the | ▁Top | ?`
- Generated answer: The answer is:

<strong>John Sayles</strong>

John Sayles is an American screenwriter, director, and actor. He is best known for his work on the films <em>The Brother from

