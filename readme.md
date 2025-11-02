<p align="center">
  <img src="images/banner.jpg" width="750" />
</p>

This work, called AlertAthlete, proposes a method to estimate a heat alert level from a set of meteorological parameters readily available for athletes and coaches. It employs machine learning (ML) in compliance with a major heat safety policy. AlertAthlete also implements the proposed ML method in a handy, wearable device to continuously track the current alert level during an athletic activity and issue early warnings for precautions and activity adjustment.

AlertAthelete uses the decision tree (DT) and random forest (RF) algorithms to build ML classifiers, which take a set of meteorological parameters as an input: temperature (F), relative humidity (%), cloud cover (%), precipitation (inch), wind speed (knot), and time of day. The classification output is one of the heat alert levels that are defined by Grundstein et al. and adopted by the National Federation of State High School Associations and its state affiliates (including Massachusetts Interscholastic Athletic Association). AlertAthelete deploys the proposed classifiers into a battery-operated ESP32 microcontroller to periodically download meteorological parameters from an online weather service and update the current alert level through deep sleep cycles. When the alert level is in the “high risk” or “extreme” condition, AlertAthelete raises a 100dB audible alarm with an on-board speaker. 

The proposed classifiers are trained with 45,777 meteorological data samples in the summer of 2024, which were collected from 290 cities in the US with an online database of the National Oceanic and Atmospheric Administration (NOAA). After hyperparameter adjustment, the DT and RF classifiers yield 91% and 99% classification accuracy in five-fold stratified cross-validation. 

AlertAthelete has been empirically tested in tennis practice and matches in the spring and summer of 2025. It can be worn easily as it is the size of an eraser and lighter than a smart watch (5/8 oz). By saving its power consumption effectively, AlertAthelete can run over six hours, which is long enough for a sports practice and matches. Their audible alarm is highly noticeable even in intensive practices and matches. 

AlertAthlete allows athletes and coaches to be aware of their heat risk to take the necessary precautions (e.g. taking breaks in the shades and extra water), lower their chances of heat-related accidents (e.g. falls and ER visits), and perform the best of their ability. 


<!--
## Publications
- Hanna Suzuki, "Integrating IoT and Machine Learning for Mobile and Wearable Heat Risk Tracking in Outdoor Sports," In *Proc. of the 29th Technological Advances in Science, Medicine, and Engineering*, poster presentation abstract, July 2025. [preprint](https://github.com/HSSBoston/alert-athlete-pro/blob/main/doc/tasme25poster.pdf)
- Hanna Suzuki, "Machine Learning-based Heat Risk Estimation for Outdoor Sports," In *Proc. of 12th International Young Researchers' Conference*, oral presentation abstract, December 2025. [preprint](https://github.com/HSSBoston/alert-athlete/blob/main/doc/iyrc25fall.pdf)
-->