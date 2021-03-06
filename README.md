**CRYPTOCURRENCIES TRADING BOT**

This projects aims at developing an algorithm with multiple components, with the intent to predict cryptocurrencies. 
Based on these predictions, a decentralized investment fund of cryptocurrencies will be established on Enzyme, with its corresponding wallet address so that it can be easily accesible for people who would like to invest.  

For this objective we   

* Scrap & clean Hour Price data through coingeko or gemini
* Scrap & clean, using PRAW, subreddits related to the selected crypto assets
* Apply Text-Sentiment analysis over the subreddit posts and merge with Price data
* Apply LSTM over the multivariate dataset
* Set an enzyme-fund over a COVAN testnet and fetch transaction costs
* Calculate ROI & Risks of changes of strategy based on the algorithms decisions - MISSING
* Set Bot transactions - MISSING
* Set code on Amazon Lambda




<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Crypto-Bot</h3>




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


The goal is to allow for people to invest on a fund governed by decisions merely taken by algorithms analysing social media and price history. 
We want to set a fund which only win minimum money to pay gas fees.  



### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Keras](https://keras.io/)
* [Tensorflow](https://www.tensorflow.org/)
* [sklearn](https://scikit-learn.org/)
* [coingecko](https://www.coingecko.com/api/documentations/v3)
* [enzyme-bot](https://medium.com/enzymefinance/building-a-trading-bot-on-enzyme-e002b6419b23/)
* [Praw](https://praw.readthedocs.io/en/stable/)
* [Praw](https://github.com/pushshift/api)






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

  Price Scrapper & Cleaner
  ```sh
   python3 Coingecko_Scrapper/Price_Scrapper.py
   ```
  Reddit Scrapper & Cleaner
  ```sh
   python python3 Reddit_Scrapper/subreddit-comments-dl/src/subreddit_downloader.py Ethereum --batch-size 50 --laps 800 --reddit-id <reddit_id> --reddit-secret <reddit_secret> --reddit-username <reddit_username> --utc-after 1589459201
   python3 Reddit_Scrapper/subreddit-comments-dl/src/dataset_builder.py 
   python3 Reddit_Scrapper/subreddit-comments-dl/dataset_formater.py
   ```
  Merge & Cleaning
  
  ```sh
   python3 Transformations.py 
   ```
  

After both have run, run the following scripts to clean and merge the data separe:




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/CRYPTO_TRADING_BOT`)
3. Commit your Changes (`git commit -m 'Add some features'`)
4. Push to the Branch (`git push origin feature/CRYPTO_TRADING_BOT`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Forked and edited works with respective licenses:
* https://github.com/pAulseperformance/cryptopanic_API_Wrapper
* https://github.com/pistocop/subreddit-comments-dl
* https://github.com/avantgardefinance/enzyme-bot


<!-- CONTACT -->
## Contact

Roberto Belarmino - robertogarx2@gmail.com
Gonzalo Etse - gonzaloetjo@gmail.com.com




<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Enzyme bot by Erin Koen](https://medium.com/enzymefinance/building-a-trading-bot-on-enzyme-e002b6419b23)
* [Reddit scrapper by pistocop](https://github.com/pistocop/subreddit-comments-dl)
