#!/usr/bin/env python3
import click
from pathlib import PurePosixPath

from src.MediaHandler import MediaHandler
from src.SearchTermMatcher import SearchTermMatcher
from src.Transcriber import Transcriber


@click.command()
@click.option('-i', '--input_file', required=True, type=click.Path(exists=True), help='Filepath to the input file')
@click.option('-o', '--output_file', required=True, type=click.Path(), help='Where the file should be saved')
@click.option('-s', '--search_term', required=True, help='The word or sentence to extract')
def extract_clip(input_file, output_file, search_term):
    audio_filename = PurePosixPath(input_file)
    output_filename = PurePosixPath(output_file)
    sentence_to_look_for = search_term

    media_handler = MediaHandler(audio_filename)
    transcriber = Transcriber(audio_filename)
    matcher = SearchTermMatcher()

    transcript = transcriber.create_transcript()
    potential_matches = matcher.find_potential_matches(sentence_to_look_for, transcript)

    closest_match = sorted(potential_matches, key=(lambda match: match.confidence), reverse=True)[0]

    media_handler.cut_and_save(output_filename, closest_match.get_start(), closest_match.get_end())


if __name__ == '__main__':
    extract_clip()
