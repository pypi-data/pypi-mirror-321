import pandas as pd
import numpy as np
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences
from statistics import mean, mode


from prediction_btc import model, tokenizer,stop_words

def preprocessing(text):
    try:
        if isinstance(text, pd.Series):
            text = text.fillna('').astype(str)  # Handle NaN values
            text = text.apply(lambda x: re.sub(r'[^a-zA-Z0-9]', ' ', x))  # Remove special characters
            text = text.apply(lambda x: " ".join(
                [word.lower() for word in x.split() if word.lower() not in stop_words]
            ))
            return text

        elif isinstance(text, str):
            text = re.sub(r'[^a-zA-Z0-9]', ' ', text)  # Remove special characters
            text = " ".join(
                [word.lower() for word in text.split() if word.lower() not in stop_words]
            )
            return text

        else:
            raise ValueError("Input harus berupa pandas Series atau string!")

    except Exception as e:
        raise ValueError(f"Error saat preprocessing: {e}")


def tokenize_and_padding(text, max_len=0):
    try:
        if isinstance(text, pd.Series):
            text = text.tolist()  # Convert to list

        if not isinstance(text, list):
            raise ValueError("Input text harus berupa list atau pandas Series")

        sequences = tokenizer.texts_to_sequences(text)

        if max_len == 0:
            sequence_lengths = [len(seq) for seq in sequences]
            average = round(mean(sequence_lengths))
            try:
                modus = mode(sequence_lengths)
            except:
                modus = 0
            max_len = average + modus

        padded_sequences = pad_sequences(sequences, maxlen=max_len)  # Perform padding
        return padded_sequences

    except Exception as e:
        raise ValueError(f"Error saat tokenisasi dan padding: {e}")


def only_prediction(tokenized):
    try:
        if isinstance(tokenized, list):
            tokenized = np.array(tokenized)

        if not isinstance(tokenized, np.ndarray):
            raise ValueError("Input tokenized harus berupa numpy array atau list")

        prediction = model.predict(tokenized)
        sentiment = (prediction >= 0.5).astype(int)

        df = pd.DataFrame({
            'prediction': prediction.flatten(), 
            'sentiment': sentiment.flatten() 
        })
        return df

    except Exception as e:
        raise ValueError(f"Error saat membuat prediksi: {e}")


def full_prediction(text):
    try:
        if not isinstance(text, (str, pd.Series)):
            raise ValueError("Input harus berupa string atau pandas Series")

        text_processed = preprocessing(text)
        sequences = tokenize_and_padding(text_processed, 0)
        results = only_prediction(sequences)

        result_df = pd.DataFrame({
            'text': text_processed,
            'padded': list(sequences),
        })

        result_df = pd.concat([result_df, results], axis=1)
        return result_df

    except Exception as e:
        raise ValueError(f"Error saat melakukan prediksi penuh: {e}")
