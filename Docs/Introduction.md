# Introduction
This project aims to help users visualise their strategies, with
a combined AI approach. Specifically, we aim to research whether
a model which synthesizes multiple AI disciplines will evaluate
and visualise user defined strategies, in near real time.
  
We will be utilising a video game environment for  this - 
specifically League of Legends - because video games have 
incredibly obvious strategies. And, they usually carry immediate
objectives. This will allow us to probe for multiple levels of 
'foresight,' as our visualisation models become more precise.

## Interface
For our users to interface with our product, they will have to be
able to review their own games, and create their own strategies.
This means we will have to provide an environment for users to
review their games, and save clips where they believe themselves
to have spotted some hidden strategical insight.
  
Once this has been done, we will utilise modern AI techniques
to consider how the gameplay may have unfolded if the user were
able to execute the strategy they imagine prior. This 
visualisation will be the first challenge of our project, and
preliminary research indicates that it can be done with some
precision.
  
In order for our users to remember their strategies, it is
important for them to have a hand in the simulation process. This
can be conceived as prompt engineering for the user. On our end
this will mean applying modern LLM techniques between simulations,
such that the user has an easily readable interface. (Or even text
to speech if we have the time).

## Our Goals
The central goal will be to ensure our visualisations of user 
strategies are as precisely in line with the real limitations of 
the game, without defaulting to a set of rules provided by the 
game, (without us having to program a skeleton of the game for our
models to use.) This will hopefully keep the user experience as
playful and creative as possible, leaving some details left to
imagine.
  
The secondary goal of this project is to compare different
models for producing visualisations, such that we can combine
said models into a more accurate picture of visual strategy.
  
Thirdly, we are interested to see that this can be done cheaply,
without the use of extremely large computers, or resources which
are expensive, both for our users and for the environment.

## Evaluation
We will be able to test the validity of the product via survey,
if the system works as expected. Prior to this, we will test the
hypothesis of our research project by constructing a medium-sized
dataset of images corresponding to visual targets (after strategy
has been deployed). 

From this, we will be capable of testing the
fine-tuned portion of our model in the traditional manner, by
splitting our dataset into training and testing portions, and 
scoring the test portions

## Work Flow
