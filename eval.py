import os

os.environ["CUDA_VISIBLE_DEVICES"]=""
os.environ["USE_CPU"]="1"

import sys
import argparse
import numpy as np
import pandas as pd
from model import train
import torch

vowels = sorted(['y', 'é', 'ö', 'a', 'i', 'å', 'u', 'ä', 'e', 'o'])

def process_test_data(test_file):
    with open(test_file, "r") as test_data:
        total_list = []
        for line in test_data:
            for character in line:
                total_list.append(character)

        total_list = ["<s>", "<s>"] + total_list + ["<e>", "<e>"]
        return total_list

def character_vector(character, char_set):
    sub_array = np.zeros(len(char_set))
    if character in char_set:
        sub_array[char_set.index(character)] = 1
    return sub_array

def create_test_data(all_chars, char_set):
    index_list = []
    vectors_list = []
    for idx in range(len(all_chars) - 4):

        # window_not_in_char_set = [
        #     x not in char_set for x in [
        #         all_chars[idx],
        #         all_chars[idx + 1],
        #         all_chars[idx + 3],
        #         all_chars[idx + 4],
        #     ]
        # ] 

        if (all_chars[idx + 2] not in vowels):# or any(window_not_in_char_set):
            continue

        vowel_index = vowels.index(all_chars[idx + 2])
        index_list.append(vowel_index)

        curr_vector = np.concatenate([
            character_vector(character, char_set) for character in 
            [
                all_chars[idx], 
                all_chars[idx + 1], 
                all_chars[idx + 3], 
                all_chars[idx + 4]
            ]
        ])
        vectors_list.append(curr_vector)

    return np.array(vectors_list), np.array(index_list)

def predict_vowels(model, input_data):
    predictions = model(torch.Tensor(input_data)).detach().numpy()
    predicted_vowels = np.argmin(np.abs(predictions), axis=1)
    return predicted_vowels
    

def accuracy(true, pred):
    accuracy = sum(true == pred) / len(pred)
    print(f"Model accuracy: {round(accuracy * 100, 2)}%")

def write_output_data(test_file, output_file, predicted_vowels):
    with open(test_file, "r") as f:
        original = f.read()

    original = list(original)
    pred_idx = 0
    for idx, char in enumerate(original):
        # if pred_idx < len(predicted_vowels):
        try:
            if char in vowels:
                original[idx] = vowels[predicted_vowels[pred_idx]]
                pred_idx +=1 
        except IndexError: 
            import pdb; pdb.set_trace()

    with open(output_file, "w") as f:
        f.write("".join(original))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("test_file", type=str)
    parser.add_argument("model_pickle", type=str)
    parser.add_argument("output_file", type=str)

    args = parser.parse_args()

    model = torch.load(args.model_pickle)
    model.eval()

    all_characters = process_test_data(args.test_file)

    test_input, true_vowel_index = create_test_data(
        all_characters, 
        model.vocab
    )

    predicted_vowel_index = predict_vowels(model, test_input)
    accuracy(true_vowel_index, predicted_vowel_index)

    write_output_data(args.test_file, args.output_file, predicted_vowel_index)

