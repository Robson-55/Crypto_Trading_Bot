**CRYPTOCURRENCIES TRADING BOT**

This projects aims at developing an algorithm composed of several pieces of code, in which some cryptocurrencies prices are predicted. Based on these predictions, an investment fund of cryptocurrencies will be established on Enzyme, with its corresponding wallet address so that it can be easily accesible for people who would like to invest.
In this project, a Reddit scrapper will be used in order to get comments and submissions from Reddit in the past years. Those news will be passed through a pretrained transformer (GPT-2) in order to analyze its sentiment score. Once this step is done, another scrapper will be used in order to get the historic of pricesand volumes from a selected set of crypto assets on a daily basis. This information will be merged with the sentiment scores for each day. After all this information is gathered, it will be passed through a deep learning LSTM model in order to be trained with it and output the price predictions for each cryptocurrency.  
For future news, Cryptopanic (news aggregator from several sources beyond Reddit) will be used. The transformer will be feeded with all this news and give as output its sentiment score, averaging by day. After this is done, this information will be merged with new daily prices, volumes... in order to keep on predicting future prices.

In this project, a Reddit scrapper will be used in order to get comments and submissions from Reddit in the past years. Those news will be passed through a pretrained transformer (GPT-2) in order to analyze its sentiment score. Once this id done, another scrapper will be used in order to get the historic of prices, volume... from a selected set of crypto assets on a daily basis. This information will be merged with the sentiment score for each day. After all this information is gathered, it will be passed through a deep learning regression model in order to be trained with it. For future news, Cryptopanic (news aggregator from several sources beyond Reddit) will be used. The transformer will be feeded with all this news and give as output its sentiment score, averaging by day. After this is done, this information will be merged with new daily prices, volumes... in order to keep on predicting future prices.

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][https://github.com/gonzaloetjo, https://github.com/Robson-55]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/gonzaloetse/]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://st3.depositphotos.com/8950810/17657/v/600/depositphotos_176577870-stock-illustration-cute-smiling-funny-robot-chat.jpg">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Tennis-Predictor</h3>

  <p align="center">
    Crypto bot:
    <br />
    <a href="https://github.com/Robson-55/Crypto_Trading_Bot/tree/main/Coingecko_Scrapper"><strong>Price Scrapper & Price data Cleaning »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Robson-55/Crypto_Trading_Bot/tree/main/Reddit_Scrapper/subreddit-comments-dl">Reddit scrapper & Data preparation</a>
    <a href="https://github.com/Robson-55/Crypto_Trading_Bot/tree/main/Reddit_Scrapper/subreddit-comments-dl">Models for Sentiment and Price Prediction</a>
    <a href="https://github.com/Robson-55/Crypto_Trading_Bot/tree/main/Reddit_Scrapper/subreddit-comments-dl">Enzyme Bot</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The goal of this project is to gain on medium term investment (1-3 months) through sentiment analysis and price analysis.



### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Keras](https://keras.io/)
* [Tensorflow](https://www.tensorflow.org/)
* [sklearn](https://scikit-learn.org/)



<!-- GETTING STARTED -->
## Getting Started

We suggest to create a virtual environment for python and continue with the installation.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Robson-55/Crypto_Trading_Bot.git
   ```

2. Install REQUIRMENT.txt packages
   ```sh
   python3 -m pip install -r requirements.txt
   ```




<!-- USAGE EXAMPLES -->
## Usage

Once Installed all requirements, run the coingecko scrapper and reddit scrappers with the following comands.

 ```sh
   python3 Coingecko_Scrapper/Price_Scrapper.py
   python python3 Reddit_Scrapper/subreddit-comments-dl/src/subreddit_downloader.py Ethereum --batch-size 50 --laps 800 --reddit-id <reddit_id> --reddit-secret <reddit_secret> --reddit-username <reddit_username> --utc-after 1589459201
   python3 Reddit_Scrapper/subreddit-comments-dl/src/dataset_builder.py 
   python3 Reddit_Scrapper/subreddit-comments-dl/dataset_formater.py
   ```

After both have run, run the following scripts to clean and merge the data separe:

1. KNN
   ```sh
   python Python/Models/KNN.py
   ```
2. LogReg
   ```sh
   python Python/Models/LogReg.py
   ```
3. NN
   ```sh
   python Python/Models/NN.py
   ```
4. LSTM
   ```sh
   python Python/Models/LSTM.py
   ```
5. SVM
   ```sh
   python Python/Models/SVM.py
   ```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/tennis-predictor`)
3. Commit your Changes (`git commit -m 'Add some features'`)
4. Push to the Branch (`git push origin feature/tennis-predictor`)
5. Open a Pull Request


