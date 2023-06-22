import ctranslate2
import jieba

# 要翻译的文本
input_text = ""

# 分词
tokenized_text = list(jieba.cut(input_text))
print(tokenized_text)

# 加载翻译模型
translator = ctranslate2.Translator("./save_models/")

# 进行翻译
translated = translator.translate_batch([tokenized_text])

# 解码翻译结果
translated_text = " ".join(translated[0].hypotheses[0])


# 输出翻译结果
print(translated_text)
