---
tags: 
---
## Physics IA2 Report 

### Finding the speed of sound by investigating the frequency of the 7th harmonic

















#### By Noah Alexiou
<div style="page-break-after: always;"></div>



























## Research Question:


Can the speed of a sound wave be accurately calculated by investigating the relationship between the frequency of the 7th harmonic of a pipe and then varying length of a pipe with open ends

## Rationale:




 The purpose of the original experiment was to calculate the speed of a sound wave in air by finding and measuring the frequency of the harmonics in a fixed length of pipe with one closed end.

The harmonic of the pipe was the independent variable and the factor that was altered in between trials that all other changes were caused by
The frequency of each harmonic was the dependent variable and first estimated using the equation $f=(273\pm5.75)n$ 

This initial value was then fine-tuned to become or confirmed to be the harmonic through listening to the pipe with one ear and determining at what frequencies it sounded loudest. By plotting the desired harmonic of the pipe that the frequency being played corresponds with on the x-axis and the current frequency being played on the y-axis, the gradient of the graph corresponds with the relationship between each harmonic and the frequency of it.
 

By substituting in the equation $f=\frac{v}{\lambda}$ , substituting in the equation, and re-arranging the formula to become $\lambda = \frac{4L}{n}$, an equation to find the speed of sound can be found. This formula is $v=\frac{n}{2L}f$ 

Where $v$ is the speed of the sound wave (m/s) and $L$ is the length of the pipe (m), the speed of sound could be found.

While this experiment was successful in calculating the speed of sound to $\pm$ $2.1$% uncertainty and $4.21$% error compared to the accepted value of 343m/s, it relied heavily on a person's ability to find the harmonic frequency by ear, which differed from person to person. This also limited the number of harmonic that were able to be tested as high frequency sounds were either too difficult to perceive, or impossible to perceive by humans. Additionally, changing the frequency being played through the speaker is an inaccurate way to find the harmonic, as resonances in the speaker itself could alter the intensity or loudness of the sound waves it creates. If possible, the change in frequency throughout the experiment should be minimized. 

Relying on human perception of sound created too many variables for it to be viable when any sort of precision is needed. Changing the frequency of the sound wave significantly was also a poor way to find the pipe's harmonic. Therefore, the experiment was modified.

A dB meter was used to determine when the pipe was tuned to a harmonic, as it could objectively and quantitatively measure sound intensity. Additionally, Instead of changing the harmonic of the sound wave to change harmonic, the length of the pipe was altered, which reduced the range of frequencies played throughout the experiment. The 7th harmonic was chosen as the target harmonic, as the frequency needed to achieve this harmonic in the given length of pipe was assumed to be within the range of the dB meter used.

The modified experiment utilizes a pipe with a plunger inside, which can be used to change the length of the cavity inside from as little as 1cm, to 30cm. This allows the independent variable to become the pipes length, and the dependent variable the frequency that the 7th harmonic occurs at. A dB meter was also utilized in order to measure sound intensity instead of the human ear, so qualitative data could be collected. This meter measured to 1 d.p.

### Diagram 1

| Risk                         | Mitigation Strategy                                            |
|:-----------------------------|:---------------------------------------------------------------|
| Hearing damage               | Use appropriate sound levels and do not place driver near ears |
| Cutting fingers on pipe burr | Handle equipment carefully and do not touch burr               |  




## Results:

### Figure 1:
![[Pasted image 20240509094336.png]]

### Figure 2

![[Pasted image 20240509234752.png]]

##### Outliers
No significant outliers were found during the collection of data. While the frequency of the 7th harmonic varied between trials, the most it ever varied was found to be only 16 Hz. 
## Analysis

##### Describe data collection process
At each pipe length, 5 trials were conducted. At the beginning of each trial, the frequency generator was set to an estimate of the frequency that the 7th harmonic should occur at.
An estimate of the 7th harmonic was found using the formula $f=\frac{7}{4}*v*\frac{1}{L}$ where $f$ is the frequency of the wave, n is the number corresponding to the harmonic being targeted, $v$ is the velocity of the wave, or the speed of sound, and $L$ is the length of the pipe. This was derived from the formula $L=\frac{n\lambda}{4}$, when $v=f\lambda$ was substituted in. The speed of sound was substituted in as 343m/s, the accepted value, and the length of the pipe was substituted in as what it was measured as at the beginning of the trial. 
Once set, the frequency would be altered in increments of $\pm1$. If the amplitude increased, the last action would be repeated. For example, if increasing the frequency from 1010 Hz to 1011 Hz increased the amplitude by a measurable amount, it would be increased again to 1012 Hz. Vise versa if increasing the frequency decreased the amplitude, it would be decreased back to its previous value and may have continued to decrease if doing to increased amplitude. The frequency that produced the highest amplitude was considered to be the true 7th harmonic of the pipe at that length. . 


The average frequency that the 7th harmonic occurs at each pipe length was the mean of  frequencies from the five trials conducted at that specific length. These average frequency values were then plotted on the y-axis, and the reciprocal of the pipe length corresponding to that average on the x-axis. A linear line of best fit was then found. This line was $y=632.87x + 53.896$. The minimum and maximum of this line were also calculated and found to be $y=577.58x + 75.37$ and $y=679.25x + -150.03$ respectively. The uncertainty of the frequency at each pipe length was found by subtracting the highest frequency recorded as the harmonic at each pipe length, then subtracting the corresponding lowest frequency from it. 

The uncertainty of the gradient was found by using the formula $\delta gradient = \frac{(max slope - min slope)}{2}$. By substituting the maximum and minimum lines of best fit $\delta gradient$ was found to be $\delta gradient = \frac{(679.25-577.58)}{2} = \pm 50.84$. Therefore, %$\delta$ is $\frac{50.84}{632.87}=$ 8.03%

Therefore, the speed of the wave was found to be $v=\frac{4*(632.87\pm50.84)-53.896}{7}=353.94m/s$. The error from the expected value was found to be %error $=\frac{353.94-343}{343}*100=3.19$% error.

### Figure 3

![[Pasted image 20240508221902.png]]



##### Relationships and trends
Since the expected relationship, $f=\frac{7}{4}*v*\frac{1}{L}$, is linear, it was clear that the line of best fit would be linear. The line of best fit for the data collected was found using Excel and as stated, this line was $y=632.87x + 53.896$. The minimum and maximum of this line were also calculated and found to be $y=577.58x + 75.37$ and $y=679.25x + -150.03$ respectively. 

A linear relationship has a constant gradient. in this case, since the gradient is the relationship between the non constant variables such as frequency of the wave, f, and its length, L. This implies that the ratio between these variables remains constant, which is the expected behavior. by substituting values for f and l into $f=\frac{7}{4}*v*\frac{1}{L}$, the speed of sound can be found. 

##### Limitations
A limitation that this experiment suffered from was a poor choice of environment. The room that the frequency of the harmonic was found in was not quiet enough which caused background noise to severely impact the meters measurements. This forced the experiment to be conducted with a combination of dB meter and human perception, which was less accurate and went against one of the key goals set when the experiment was modified. Another limitation that impacted the experiment's results was the inconsistent position of the speaker driver. The position of the driver in all directions varied throughout all tests due to the lack of a solid mount or jig. The same goes for the dB meter. Moving the speaker driver will impact how standing waves form in the pipe. Changing the position of the dB meter will affect the intensity of the wave it detects. 

## Evaluation:

The research question was somewhat was answered as it was found that the speed of sound can be calculated by investigating the relationship between the frequency of the 7th harmonic of a pipe and then varying length of a pipe with open ends but with questionable accuracy. 


The speed of sound was found to be 353.94m/s with 3.19% error. Some reasons for this difference are the limitations discussed such as the inconsistent driver position and suboptimal measuring of the frequency of the 7th harmonic. 3.19% is a relatively low error, but it must be considered whether this error was the result of correct procedure or not. 

Potential extension to this experiment could be the investigation of how the air in the pipe affects the speed of sound. By measuring the speed of sound at different temperatures and air densities, the relationship between these factors and the speed of sound could be determined 



 
## Conclusion:

This experiment aimed to determine the speed of sound by investigating the relationship between the frequency of the 7th harmonic and the length of a pipe with open ends. The results showed a linear relationship, which allowed the speed of sound to be calculated. Limitations such as environmental noise and changes in the experimental setup over the course of the experiment caused error to a limited degree. Potential extensions to this experiment could investigate how environmental factors influence the speed of sound in air. 


## Sources




