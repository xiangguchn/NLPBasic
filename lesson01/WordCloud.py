# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 08:34:33 2020

@author: xiangguchn
"""

import jieba
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# string used to generate word cloud
string = """
在上周五刚刚结束的挑战的法则中由潘玮柏大张伟戚薇乔杉刘维于小彤组成的首发嘉宾阵容在经过第一期户外挑战和比拼之后迎来了他们首次舞台表演潘玮柏首发登场霸气演绎分裂的时光超完美表演惊艳全场当晚6位嘉宾纷纷放大招拿出自己最擅长的绝技为观众呈现了一场最完美的演出潘玮柏首发登场经典歌曲被遗忘的时光24个比利的全新改编演绎分裂的时光在原曲嘻哈流行的基础上加入弦乐伴奏与合唱团搭配瞬间气势磅礴充满张力尤其独有的潘氏低音炮一开嗓就引发全场尖叫苏到极致让人见识到什么是开口跪系列舞台上的潘玮柏霸气侧漏气场十足特别是高潮处呈现出的那种撕心裂肺的感觉仿佛能把人带到歌的故事里去这个改编跟原曲比起来节奏放缓了却在这缓慢抒情的演绎中又不缺乏爆发力像在对人们诉说着他的音乐他的追求超震撼演绎瞬间引发网友热议这个版本的24个比利太震撼了现场还是那么稳从头赞到尾的表演低音好撩人实力没得说不愧为初代偶像超级帅的现场很有感觉男神魅力依旧不减啊现场是真的稳
"""
# How many percentage of total words will be used to genrate word cloud
ratio = 0.25

# get words inclued in the string with jieba.cut
words = list(jieba.cut(string))

# calculate tfidf value for every word and assign them to dictionarly
tfidf_value = dict()
for word in words:
    # count the number of word in string
    tf = string.count(word)
    # whether word in words
    # idf = 1/(np.log10(sum(1 for s in words if word in s)/tf) + 1e-6)
    idf = 1/(np.log10(sum(1 for s in words if word in s)) + 1e-6)
    # calculate rate of word and assign them to dic of tfidf_value
    tfidf_value[word] = tf*idf   
# word_importance is a list 
words_importance = sorted(tfidf_value.items(), key=lambda x: x[1], reverse=True)[:int(len(tfidf_value)*ratio)]

# crate one wordcloud canvas, Font_path must be correct to system
wc = WordCloud(background_color="black", max_words=1000, font_path='fonts/simfang.ttf')
# use generate_from_frequencies to generate frequencies for words
wc.generate_from_frequencies({w: v for w, v in words_importance})
# plot word cloud
plt.imshow(wc)
