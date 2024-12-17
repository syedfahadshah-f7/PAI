import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.models import Word2Vec
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('punkt_tab') # added this line to download punkt_tab
Lem = WordNetLemmatizer()
Sp = set(stopwords.words("english"))
para = "The beauty of curiosity lies in its boundless nature, sparking a desire to explore the unknown and uncover hidden truths. It’s the force that drives innovation, propels learning, and bridges gaps between imagination and reality. From the vastness of the cosmos to the intricate design of a leaf, curiosity invites us to question, understand, and marvel. It’s not just about finding answers but about embracing the journey of discovery, where every step uncovers new possibilities and perspectives. In a world brimming with mysteries, curiosity keeps our spirit alive, reminding us that there’s always more to learn and experience."

sent = sent_tokenize(para)

for i in range(0,len(sent)):
    words = word_tokenize(sent[i])
    lem_word = [Lem.lemmatize(word)  for word in words if word not in Sp]
    sent[i] = lem_word
    

model = Word2Vec(sent,min_count=1)
print(model.wv["boundless"],"\n")
print(model.wv.most_similar("curiosity"))
