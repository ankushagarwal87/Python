import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import movie_reviews


def testTokenizer(example_sent):
    print(sent_tokenize(example_sent))
    print(word_tokenize(example_sent))


def testStopWords(example_sent):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(example_sent)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    print(word_tokens)
    print(filtered_sentence)


def testStemming(example_sent):
    ps = PorterStemmer()
    words = word_tokenize(example_sent)
    for w in words:
        print(ps.stem(w))

def testPOSTagging():
    train_text = state_union.raw("2005-GWBush.txt")
    sample_text = state_union.raw("2006-GWBush.txt")
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    try:
        for i in tokenized[:5]:
            #print(i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #print(tagged)
            #testChunking(tagged)
            #testChinking(tagged)
            testNER(tagged)

    except Exception as e:
        print(str(e))


def testChunking(tagged):
    #chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    #tagged = nltk.pos_tag(words)
    chunkGram = r"""NP: {<DT>?<JJ>*<NN.?>*}
                     P: {<IN>}
                     V: {<VB.?>}
                    PP: {<P><NP>}
                    VP: {<V><NP|PP>*}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print(chunked)
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        print(subtree)
    chunked.draw()


def testChinking(tagged):
    chunkGram = r"""Chunk: {<.*>+}
                                  }<VB.?|IN|DT|TO>+{"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(tagged)
    print(chunked)
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        print(subtree)
    chunked.draw()


def testNER(tagged):
    namedEnt = nltk.ne_chunk(tagged, binary=False)
    namedEnt.draw()


def testLemmatizing():
    lemmatizer = WordNetLemmatizer()
    print(lemmatizer.lemmatize("cats"))
    print(lemmatizer.lemmatize("cacti"))
    print(lemmatizer.lemmatize("geese"))
    print(lemmatizer.lemmatize("rocks"))
    print(lemmatizer.lemmatize("python"))
    print(lemmatizer.lemmatize("better", pos="a"))
    print(lemmatizer.lemmatize("best", pos="a"))
    print(lemmatizer.lemmatize("run"))
    print(lemmatizer.lemmatize("run",'v'))

def testWordNet():
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets("good"):
        #print(syn)
        for l in syn.lemmas():
            #print(l.name())
            synonyms.append(l.name())
            if l.antonyms():
                #print(l.antonyms())
                antonyms.append(l.antonyms()[0].name())
    #print(set(synonyms))
    #print(set(antonyms))
    w1 = wordnet.synset('ship.n.01')
    w2 = wordnet.synset('boat.n.01')
    print(w1.wup_similarity(w2))
    w1 = wordnet.synset('ship.n.01')
    w2 = wordnet.synset('car.n.01')
    print(w1.wup_similarity(w2))



example_sent = "This is a sample sentence, showing off the stop words filtration."
#testTokenizer(example_sent)
#testStopWords(example_sent)
#testStemming(example_sent)
#testPOSTagging()
#example_sent= "Mr Obama played a big role in the Health Insurance Bill"
#testChunking(word_tokenize(example_sent))
#testLemmatizing()
testWordNet()




