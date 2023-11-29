# paperqa-zotero
Allows you to train a local LLM on your Zotero files. It will return sources.

---

## how to use
### zotero
To download papers, you need to get an API key for your Zotero account.

Get your library ID, and set it as the environment variable `ZOTERO_USER_ID`.

For personal libraries, this ID is given [here](https://www.zotero.org/settings/keys) at the part "Your userID for use in API calls is XXXXXX".

For group libraries, go to your group page https://www.zotero.org/groups/groupname, and hover over the settings link. The ID is the integer after /groups/. (h/t pyzotero!)

Create a new API key [here](https://www.zotero.org/settings/keys/new) and set it as the environment variable `ZOTERO_API_KEY`.
The key will need read access to the library.

### ollama
install ollama and pull a model, i used `llama2:7b`.

### install requirements

`pip install -r requirements.txt``

### run
`python main.py``

---

## result
Question: What advantages are unique to bitcoin and how can these advantages help investors?, please cite the sources of your information and create a reference table of sources.

Advantages of Bitcoin:

1. Decentralization: Bitcoin is decentralized, meaning that there is no central authority controlling it. Transactions are recorded on a public ledger called the blockchain, which is maintained by a network of computers around the world. (Q1)
2. Security: Bitcoin transactions are secure and cannot be reversed or tampered with. The blockchain technology used in Bitcoin ensures that all transactions are verified and recorded accurately. (Q2)
3. Accessibility: Anyone with an internet connection can use Bitcoin, regardless of their location or financial status. (Q3)
4. Limited supply: There will only ever be 21 million Bitcoins in existence, which means that the value of each Bitcoin could increase over time as demand for it grows. (Q4)
5. Fast and cheap transactions: Bitcoin transactions are processed quickly and at a lower cost compared to traditional payment methods. (Q5)

How these advantages can help investors:

1. Diversification: Investing in Bitcoin can provide diversification benefits as it is a unique asset class that performs differently than traditional assets such as stocks or bonds. (Q6)
2. Potential for high returns: The limited supply of Bitcoin and the increasing demand for it could lead to significant appreciation in value over time, providing potential for high returns on investment. (Q7)
3. Decentralized and secure: As Bitcoin is decentralized and secure, investors can have confidence that their investments are protected from fraud or cyber threats. (Q8)
4. Accessibility and ease of use: Anyone with an internet connection can use Bitcoin, making it easy to invest and manage assets. (Q9)
5. Limited supply: The limited supply of Bitcoin means that the value of each Bitcoin could increase over time as demand for it grows, providing potential for long-term appreciation in value. (Q10)

References:

Balutel, D., et al. "Bitcoin Awareness, Ownership, and Use: 2016–20." Bank of Canada Staff Discussion Paper, no. 2022-10, 2023.

Hougan, J., et al. "CryptoAssetsTheGuide to Bitcoin, Blockchain, and Cryptocurrency for Investment Professionals." [City, State]: CFA Institute Research Foundation, 2023.

Note: The references provided are from the text itself, which serves as the primary source for the information presented in this summary.