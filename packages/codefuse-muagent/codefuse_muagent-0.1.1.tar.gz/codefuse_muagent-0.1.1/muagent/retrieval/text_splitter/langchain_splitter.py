import os
import importlib
from loguru import logger

from langchain.document_loaders.base import BaseLoader
from langchain.text_splitter import (
    SpacyTextSplitter, RecursiveCharacterTextSplitter
)

# from configs.model_config import (
#     CHUNK_SIZE,
#     OVERLAP_SIZE,
#     ZH_TITLE_ENHANCE
# )
from muagent.utils.path_utils import *



class LCTextSplitter:
    '''langchain textsplitter 执行file2text'''
    def __init__(
            self, filepath: str, text_splitter_name: str = None,
            chunk_size: int = 500, 
            overlap_size: int = 50
    ):
        self.filepath = filepath
        self.ext = os.path.splitext(filepath)[-1].lower()
        self.text_splitter_name = text_splitter_name
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size
        if self.ext not in SUPPORTED_EXTS:
            raise ValueError(f"暂未支持的文件格式 {self.ext}")
        self.document_loader_name = get_LoaderClass(self.ext)

    def file2text(self, ):
        loader = self._load_document()
        text_splitter = self._load_text_splitter()
        if self.document_loader_name in ["JSONLoader", "JSONLLoader"]:
            # docs = loader.load()
            docs = loader.load_and_split(text_splitter)
            # logger.debug(f"please check your file can be loaded, docs.lens {len(docs)}")
        else:
            docs = loader.load_and_split(text_splitter)

        return docs

    def _load_document(self, ) -> BaseLoader:
        DocumentLoader = EXT2LOADER_DICT[self.ext]
        if self.document_loader_name == "UnstructuredFileLoader":
            loader = DocumentLoader(self.filepath, autodetect_encoding=True)
        else:
            loader = DocumentLoader(self.filepath)
        return loader
    
    def _load_text_splitter(self, ):
        try:
            if self.text_splitter_name is None:
                text_splitter = SpacyTextSplitter(
                    pipeline="zh_core_web_sm",
                    chunk_size=self.chunk_size,
                    chunk_overlap=self.overlap_size,
                )
                self.text_splitter_name = "SpacyTextSplitter"
            # elif self.document_loader_name in ["JSONLoader", "JSONLLoader"]:
            #     text_splitter = None
            else:
                text_splitter_module = importlib.import_module('langchain.text_splitter')
                TextSplitter = getattr(text_splitter_module, self.text_splitter_name)
                text_splitter = TextSplitter(
                    chunk_size=self.chunk_size,
                    chunk_overlap=self.overlap_size)
        except Exception as e:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size,
                chunk_overlap=self.overlap_size,
            )
        return text_splitter
