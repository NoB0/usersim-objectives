"""Script to translate the MG-ShopDial dataset to QRFA format."""

import argparse
import json
from typing import List

import pandas as pd

DEFAULT_INPUT_FILE = "data/MGShopDial.json"
DEFAULT_OUTPUT_FILE = "data/annotated_datasets/5_mgshopdial_updated.csv"

INTENT_ALIGNMENT = {
    "S": {
        "R": ["greeting", "interaction", "clarify", "o_question", "elicit"],
        "A": ["recommend", "answer", "explain"],
    },
    "U": {
        "Q": ["greeting", "interaction", "disclose", "o_question", "answer"],
        "F": ["pf", "nf", "explain"],
    },
}


def translate_utterance_intents(participant: str, intents: List[str]) -> str:
    """Translates the intents of the utterance to QRFA format.

    Args:
        participant: Author of the utterance.
        intents: Utterance intents.

    Returns:
        QRFA formatted intent.
    """
    qrfa_intents = set()
    for intent in intents:
        for qrfa_intent, intent_list in INTENT_ALIGNMENT[participant].items():
            if intent in intent_list:
                qrfa_intents.add(qrfa_intent)
    return "+".join(qrfa_intents)


def parse_args() -> argparse.Namespace:
    """Parses command line arguments.

    Returns:
        Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Translate MG-ShopDial dataset to QRFA format."
    )
    parser.add_argument(
        "-i",
        "--input_file",
        type=str,
        default=DEFAULT_INPUT_FILE,
        help="Path to the input file.",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=str,
        default=DEFAULT_OUTPUT_FILE,
        help="Path to the output file.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    with open(args.input_file, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(columns=["case ID", "utterance ID", "resource", "new"])

    for dialogue in data:
        case_id = dialogue["id"]
        for utterance in dialogue["utterances"]:
            utterance_id = utterance["utterance_id"]
            participant = "S" if utterance["participant"] == "Wizard" else "U"
            intents = [intent[0] for intent in utterance["intents"]]
            qrfa_intents = translate_utterance_intents(participant, intents)
            df = pd.concat(
                [
                    df,
                    pd.DataFrame(
                        [[case_id, utterance_id, participant, qrfa_intents]],
                        columns=df.columns,
                    ),
                ]
            )

    df.to_csv(args.output_file, index=False)
