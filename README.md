# Quantifying Tennis Player Performance Using Machine Learning

This project was created for the HDSI Undergraduate Scholarship. 

Creators: Karthik Guruvayurappan, Eric Jiang, Shweta Kumar

Mentor: Lauren Green

## Introduction

The goal of this project is to generate tools built on machine learning analytics and insights to improve tennis player performance, specifically for the
UC San Diego Men's Tennis Team. To generate these tools, we used data from Catapult wearable devices and In/Out on-court cameras. Through these technologies,
we constructed a time series analysis tool for swing detection, and a tool that enables point playback with information about each shot available. 

## Data Collection

Initially, for our data collection, we planned to gather data from the UC San Diego Men's Tennis Team, through synchronizing the Catapult wearable device data with the shot information provided by the In/Out on-court cameras. However, due to the COVID-19 pandemic, and the closing of tennis courts, we were unable to collect synchronized data from the Catapult wearable devices and the In/Out on-court cameras. 

Alternatively, for our data collection, due to the COVID-19 pandemic, we used mainly our datasets from testing the devices. For the Catapult devices, we collected data across two different practice sessions (containing a variety of tennis drills and points), and one shadow swinging (swinging the racket without hitting tennis balls) session to assist with our swing detection portion of the project. For the shadow swinging dataset, we included a variety of forehand and backhand swings, including slices, approach shots, low shots, lobs, and high shots. For the In/Out camera devices, we collected data for the one test session that we had, which included short court rallies, full court rallies, and serves with returns. Though this resulted in significantly less datasets than we had initially hoped for, we  still tried to draw valuable insights from these datasets. 

## Results

#### Swing Detection

The goal of our swing detection tool was to see if we could use the 100hz (100 data points per second), to generate a distribution of the different shot types that a player made during a practice session or match based on the Catapult wearable devices. To create our swing detection analysis, we used our shadow swinging dataset. Since the tennis swing involves significant hip rotation (clockwise for backhands and counter-clockwise for forehands), we selected yaw rotation (rotation around the z-axis) as one of our primary metrics to explore. For the yaw rotation in backhands, since counter-clockwise rotation is the positive direction, we expected to see slow increases in the positive direction, followed by quick spikes in the negative direction as the swing makes contact with the ball. We expected to see the reverse of this for forehand swings. 

This is the graph of the backhand yaw rotation:

![backhand timestamp vs. yaw_rotation](/Results/backhand_yaw_rotation.png)

Another metric that we chose is Catapult's smoother player load metric, since tennis swings generally begin with slower movements, and then rapidly increase as the tennis ball approaches. Therefore, in the smoothed player load graphs, we expected to see 
