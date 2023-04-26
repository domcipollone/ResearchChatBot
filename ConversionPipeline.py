from haystack.nodes import PDFToTextConverter


if __name__ == "__main__":

    converter = PDFToTextConverter(
        remove_numeric_tables=True,
        valid_languages=["de","en"]
    )
    
