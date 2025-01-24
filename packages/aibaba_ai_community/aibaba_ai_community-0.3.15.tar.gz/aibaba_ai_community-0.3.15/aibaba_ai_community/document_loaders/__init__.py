"""**Document Loaders**  are classes to load Documents.

**Document Loaders** are usually used to load a lot of Documents in a single run.

**Class hierarchy:**

.. code-block::

    BaseLoader --> <name>Loader  # Examples: TextLoader, UnstructuredFileLoader

**Main helpers:**

.. code-block::

    Document, <name>TextSplitter
"""

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aibaba_ai_community.document_loaders.acreom import (
        AcreomLoader,
    )
    from aibaba_ai_community.document_loaders.airbyte import (
        AirbyteCDKLoader,
        AirbyteGongLoader,
        AirbyteHubspotLoader,
        AirbyteSalesforceLoader,
        AirbyteShopifyLoader,
        AirbyteStripeLoader,
        AirbyteTypeformLoader,
        AirbyteZendeskSupportLoader,
    )
    from aibaba_ai_community.document_loaders.airbyte_json import (
        AirbyteJSONLoader,
    )
    from aibaba_ai_community.document_loaders.airtable import (
        AirtableLoader,
    )
    from aibaba_ai_community.document_loaders.apify_dataset import (
        ApifyDatasetLoader,
    )
    from aibaba_ai_community.document_loaders.arcgis_loader import (
        ArcGISLoader,
    )
    from aibaba_ai_community.document_loaders.arxiv import (
        ArxivLoader,
    )
    from aibaba_ai_community.document_loaders.assemblyai import (
        AssemblyAIAudioLoaderById,
        AssemblyAIAudioTranscriptLoader,
    )
    from aibaba_ai_community.document_loaders.astradb import (
        AstraDBLoader,
    )
    from aibaba_ai_community.document_loaders.async_html import (
        AsyncHtmlLoader,
    )
    from aibaba_ai_community.document_loaders.athena import (
        AthenaLoader,
    )
    from aibaba_ai_community.document_loaders.azlyrics import (
        AZLyricsLoader,
    )
    from aibaba_ai_community.document_loaders.azure_ai_data import (
        AzureAIDataLoader,
    )
    from aibaba_ai_community.document_loaders.azure_blob_storage_container import (
        AzureBlobStorageContainerLoader,
    )
    from aibaba_ai_community.document_loaders.azure_blob_storage_file import (
        AzureBlobStorageFileLoader,
    )
    from aibaba_ai_community.document_loaders.bibtex import (
        BibtexLoader,
    )
    from aibaba_ai_community.document_loaders.bigquery import (
        BigQueryLoader,
    )
    from aibaba_ai_community.document_loaders.bilibili import (
        BiliBiliLoader,
    )
    from aibaba_ai_community.document_loaders.blackboard import (
        BlackboardLoader,
    )
    from aibaba_ai_community.document_loaders.blob_loaders import (
        Blob,
        BlobLoader,
        CloudBlobLoader,
        FileSystemBlobLoader,
        YoutubeAudioLoader,
    )
    from aibaba_ai_community.document_loaders.blockchain import (
        BlockchainDocumentLoader,
    )
    from aibaba_ai_community.document_loaders.brave_search import (
        BraveSearchLoader,
    )
    from aibaba_ai_community.document_loaders.browserbase import (
        BrowserbaseLoader,
    )
    from aibaba_ai_community.document_loaders.browserless import (
        BrowserlessLoader,
    )
    from aibaba_ai_community.document_loaders.cassandra import (
        CassandraLoader,
    )
    from aibaba_ai_community.document_loaders.chatgpt import (
        ChatGPTLoader,
    )
    from aibaba_ai_community.document_loaders.chm import (
        UnstructuredCHMLoader,
    )
    from aibaba_ai_community.document_loaders.chromium import (
        AsyncChromiumLoader,
    )
    from aibaba_ai_community.document_loaders.college_confidential import (
        CollegeConfidentialLoader,
    )
    from aibaba_ai_community.document_loaders.concurrent import (
        ConcurrentLoader,
    )
    from aibaba_ai_community.document_loaders.confluence import (
        ConfluenceLoader,
    )
    from aibaba_ai_community.document_loaders.conllu import (
        CoNLLULoader,
    )
    from aibaba_ai_community.document_loaders.couchbase import (
        CouchbaseLoader,
    )
    from aibaba_ai_community.document_loaders.csv_loader import (
        CSVLoader,
        UnstructuredCSVLoader,
    )
    from aibaba_ai_community.document_loaders.cube_semantic import (
        CubeSemanticLoader,
    )
    from aibaba_ai_community.document_loaders.datadog_logs import (
        DatadogLogsLoader,
    )
    from aibaba_ai_community.document_loaders.dataframe import (
        DataFrameLoader,
    )
    from aibaba_ai_community.document_loaders.dedoc import (
        DedocAPIFileLoader,
        DedocFileLoader,
    )
    from aibaba_ai_community.document_loaders.diffbot import (
        DiffbotLoader,
    )
    from aibaba_ai_community.document_loaders.directory import (
        DirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.discord import (
        DiscordChatLoader,
    )
    from aibaba_ai_community.document_loaders.doc_intelligence import (
        AzureAIDocumentIntelligenceLoader,
    )
    from aibaba_ai_community.document_loaders.docugami import (
        DocugamiLoader,
    )
    from aibaba_ai_community.document_loaders.docusaurus import (
        DocusaurusLoader,
    )
    from aibaba_ai_community.document_loaders.dropbox import (
        DropboxLoader,
    )
    from aibaba_ai_community.document_loaders.duckdb_loader import (
        DuckDBLoader,
    )
    from aibaba_ai_community.document_loaders.email import (
        OutlookMessageLoader,
        UnstructuredEmailLoader,
    )
    from aibaba_ai_community.document_loaders.epub import (
        UnstructuredEPubLoader,
    )
    from aibaba_ai_community.document_loaders.etherscan import (
        EtherscanLoader,
    )
    from aibaba_ai_community.document_loaders.evernote import (
        EverNoteLoader,
    )
    from aibaba_ai_community.document_loaders.excel import (
        UnstructuredExcelLoader,
    )
    from aibaba_ai_community.document_loaders.facebook_chat import (
        FacebookChatLoader,
    )
    from aibaba_ai_community.document_loaders.fauna import (
        FaunaLoader,
    )
    from aibaba_ai_community.document_loaders.figma import (
        FigmaFileLoader,
    )
    from aibaba_ai_community.document_loaders.firecrawl import (
        FireCrawlLoader,
    )
    from aibaba_ai_community.document_loaders.gcs_directory import (
        GCSDirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.gcs_file import (
        GCSFileLoader,
    )
    from aibaba_ai_community.document_loaders.geodataframe import (
        GeoDataFrameLoader,
    )
    from aibaba_ai_community.document_loaders.git import (
        GitLoader,
    )
    from aibaba_ai_community.document_loaders.gitbook import (
        GitbookLoader,
    )
    from aibaba_ai_community.document_loaders.github import (
        GithubFileLoader,
        GitHubIssuesLoader,
    )
    from aibaba_ai_community.document_loaders.glue_catalog import (
        GlueCatalogLoader,
    )
    from aibaba_ai_community.document_loaders.google_speech_to_text import (
        GoogleSpeechToTextLoader,
    )
    from aibaba_ai_community.document_loaders.googledrive import (
        GoogleDriveLoader,
    )
    from aibaba_ai_community.document_loaders.gutenberg import (
        GutenbergLoader,
    )
    from aibaba_ai_community.document_loaders.hn import (
        HNLoader,
    )
    from aibaba_ai_community.document_loaders.html import (
        UnstructuredHTMLLoader,
    )
    from aibaba_ai_community.document_loaders.html_bs import (
        BSHTMLLoader,
    )
    from aibaba_ai_community.document_loaders.hugging_face_dataset import (
        HuggingFaceDatasetLoader,
    )
    from aibaba_ai_community.document_loaders.hugging_face_model import (
        HuggingFaceModelLoader,
    )
    from aibaba_ai_community.document_loaders.ifixit import (
        IFixitLoader,
    )
    from aibaba_ai_community.document_loaders.image import (
        UnstructuredImageLoader,
    )
    from aibaba_ai_community.document_loaders.image_captions import (
        ImageCaptionLoader,
    )
    from aibaba_ai_community.document_loaders.imsdb import (
        IMSDbLoader,
    )
    from aibaba_ai_community.document_loaders.iugu import (
        IuguLoader,
    )
    from aibaba_ai_community.document_loaders.joplin import (
        JoplinLoader,
    )
    from aibaba_ai_community.document_loaders.json_loader import (
        JSONLoader,
    )
    from aibaba_ai_community.document_loaders.kinetica_loader import KineticaLoader
    from aibaba_ai_community.document_loaders.lakefs import (
        LakeFSLoader,
    )
    from aibaba_ai_community.document_loaders.larksuite import (
        LarkSuiteDocLoader,
    )
    from aibaba_ai_community.document_loaders.llmsherpa import (
        LLMSherpaFileLoader,
    )
    from aibaba_ai_community.document_loaders.markdown import (
        UnstructuredMarkdownLoader,
    )
    from aibaba_ai_community.document_loaders.mastodon import (
        MastodonTootsLoader,
    )
    from aibaba_ai_community.document_loaders.max_compute import (
        MaxComputeLoader,
    )
    from aibaba_ai_community.document_loaders.mediawikidump import (
        MWDumpLoader,
    )
    from aibaba_ai_community.document_loaders.merge import (
        MergedDataLoader,
    )
    from aibaba_ai_community.document_loaders.mhtml import (
        MHTMLLoader,
    )
    from aibaba_ai_community.document_loaders.modern_treasury import (
        ModernTreasuryLoader,
    )
    from aibaba_ai_community.document_loaders.mongodb import (
        MongodbLoader,
    )
    from aibaba_ai_community.document_loaders.needle import (
        NeedleLoader,
    )
    from aibaba_ai_community.document_loaders.news import (
        NewsURLLoader,
    )
    from aibaba_ai_community.document_loaders.notebook import (
        NotebookLoader,
    )
    from aibaba_ai_community.document_loaders.notion import (
        NotionDirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.notiondb import (
        NotionDBLoader,
    )
    from aibaba_ai_community.document_loaders.obs_directory import (
        OBSDirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.obs_file import (
        OBSFileLoader,
    )
    from aibaba_ai_community.document_loaders.obsidian import (
        ObsidianLoader,
    )
    from aibaba_ai_community.document_loaders.odt import (
        UnstructuredODTLoader,
    )
    from aibaba_ai_community.document_loaders.onedrive import (
        OneDriveLoader,
    )
    from aibaba_ai_community.document_loaders.onedrive_file import (
        OneDriveFileLoader,
    )
    from aibaba_ai_community.document_loaders.open_city_data import (
        OpenCityDataLoader,
    )
    from aibaba_ai_community.document_loaders.oracleadb_loader import (
        OracleAutonomousDatabaseLoader,
    )
    from aibaba_ai_community.document_loaders.oracleai import (
        OracleDocLoader,
        OracleTextSplitter,
    )
    from aibaba_ai_community.document_loaders.org_mode import (
        UnstructuredOrgModeLoader,
    )
    from aibaba_ai_community.document_loaders.pdf import (
        AmazonTextractPDFLoader,
        DedocPDFLoader,
        MathpixPDFLoader,
        OnlinePDFLoader,
        PagedPDFSplitter,
        PDFMinerLoader,
        PDFMinerPDFasHTMLLoader,
        PDFPlumberLoader,
        PyMuPDFLoader,
        PyPDFDirectoryLoader,
        PyPDFium2Loader,
        PyPDFLoader,
        UnstructuredPDFLoader,
    )
    from aibaba_ai_community.document_loaders.pebblo import (
        PebbloSafeLoader,
        PebbloTextLoader,
    )
    from aibaba_ai_community.document_loaders.polars_dataframe import (
        PolarsDataFrameLoader,
    )
    from aibaba_ai_community.document_loaders.powerpoint import (
        UnstructuredPowerPointLoader,
    )
    from aibaba_ai_community.document_loaders.psychic import (
        PsychicLoader,
    )
    from aibaba_ai_community.document_loaders.pubmed import (
        PubMedLoader,
    )
    from aibaba_ai_community.document_loaders.pyspark_dataframe import (
        PySparkDataFrameLoader,
    )
    from aibaba_ai_community.document_loaders.python import (
        PythonLoader,
    )
    from aibaba_ai_community.document_loaders.readthedocs import (
        ReadTheDocsLoader,
    )
    from aibaba_ai_community.document_loaders.recursive_url_loader import (
        RecursiveUrlLoader,
    )
    from aibaba_ai_community.document_loaders.reddit import (
        RedditPostsLoader,
    )
    from aibaba_ai_community.document_loaders.roam import (
        RoamLoader,
    )
    from aibaba_ai_community.document_loaders.rocksetdb import (
        RocksetLoader,
    )
    from aibaba_ai_community.document_loaders.rss import (
        RSSFeedLoader,
    )
    from aibaba_ai_community.document_loaders.rst import (
        UnstructuredRSTLoader,
    )
    from aibaba_ai_community.document_loaders.rtf import (
        UnstructuredRTFLoader,
    )
    from aibaba_ai_community.document_loaders.s3_directory import (
        S3DirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.s3_file import (
        S3FileLoader,
    )
    from aibaba_ai_community.document_loaders.scrapfly import (
        ScrapflyLoader,
    )
    from aibaba_ai_community.document_loaders.scrapingant import (
        ScrapingAntLoader,
    )
    from aibaba_ai_community.document_loaders.sharepoint import (
        SharePointLoader,
    )
    from aibaba_ai_community.document_loaders.sitemap import (
        SitemapLoader,
    )
    from aibaba_ai_community.document_loaders.slack_directory import (
        SlackDirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.snowflake_loader import (
        SnowflakeLoader,
    )
    from aibaba_ai_community.document_loaders.spider import (
        SpiderLoader,
    )
    from aibaba_ai_community.document_loaders.spreedly import (
        SpreedlyLoader,
    )
    from aibaba_ai_community.document_loaders.sql_database import (
        SQLDatabaseLoader,
    )
    from aibaba_ai_community.document_loaders.srt import (
        SRTLoader,
    )
    from aibaba_ai_community.document_loaders.stripe import (
        StripeLoader,
    )
    from aibaba_ai_community.document_loaders.surrealdb import (
        SurrealDBLoader,
    )
    from aibaba_ai_community.document_loaders.telegram import (
        TelegramChatApiLoader,
        TelegramChatFileLoader,
        TelegramChatLoader,
    )
    from aibaba_ai_community.document_loaders.tencent_cos_directory import (
        TencentCOSDirectoryLoader,
    )
    from aibaba_ai_community.document_loaders.tencent_cos_file import (
        TencentCOSFileLoader,
    )
    from aibaba_ai_community.document_loaders.tensorflow_datasets import (
        TensorflowDatasetLoader,
    )
    from aibaba_ai_community.document_loaders.text import (
        TextLoader,
    )
    from aibaba_ai_community.document_loaders.tidb import (
        TiDBLoader,
    )
    from aibaba_ai_community.document_loaders.tomarkdown import (
        ToMarkdownLoader,
    )
    from aibaba_ai_community.document_loaders.toml import (
        TomlLoader,
    )
    from aibaba_ai_community.document_loaders.trello import (
        TrelloLoader,
    )
    from aibaba_ai_community.document_loaders.tsv import (
        UnstructuredTSVLoader,
    )
    from aibaba_ai_community.document_loaders.twitter import (
        TwitterTweetLoader,
    )
    from aibaba_ai_community.document_loaders.unstructured import (
        UnstructuredAPIFileIOLoader,
        UnstructuredAPIFileLoader,
        UnstructuredFileIOLoader,
        UnstructuredFileLoader,
    )
    from aibaba_ai_community.document_loaders.url import (
        UnstructuredURLLoader,
    )
    from aibaba_ai_community.document_loaders.url_playwright import (
        PlaywrightURLLoader,
    )
    from aibaba_ai_community.document_loaders.url_selenium import (
        SeleniumURLLoader,
    )
    from aibaba_ai_community.document_loaders.vsdx import (
        VsdxLoader,
    )
    from aibaba_ai_community.document_loaders.weather import (
        WeatherDataLoader,
    )
    from aibaba_ai_community.document_loaders.web_base import (
        WebBaseLoader,
    )
    from aibaba_ai_community.document_loaders.whatsapp_chat import (
        WhatsAppChatLoader,
    )
    from aibaba_ai_community.document_loaders.wikipedia import (
        WikipediaLoader,
    )
    from aibaba_ai_community.document_loaders.word_document import (
        Docx2txtLoader,
        UnstructuredWordDocumentLoader,
    )
    from aibaba_ai_community.document_loaders.xml import (
        UnstructuredXMLLoader,
    )
    from aibaba_ai_community.document_loaders.xorbits import (
        XorbitsLoader,
    )
    from aibaba_ai_community.document_loaders.youtube import (
        GoogleApiClient,
        GoogleApiYoutubeLoader,
        YoutubeLoader,
    )
    from aibaba_ai_community.document_loaders.yuque import (
        YuqueLoader,
    )


_module_lookup = {
    "AZLyricsLoader": "aibaba_ai_community.document_loaders.azlyrics",
    "AcreomLoader": "aibaba_ai_community.document_loaders.acreom",
    "AirbyteCDKLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteGongLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteHubspotLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteJSONLoader": "aibaba_ai_community.document_loaders.airbyte_json",
    "AirbyteSalesforceLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteShopifyLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteStripeLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteTypeformLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirbyteZendeskSupportLoader": "aibaba_ai_community.document_loaders.airbyte",
    "AirtableLoader": "aibaba_ai_community.document_loaders.airtable",
    "AmazonTextractPDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "ApifyDatasetLoader": "aibaba_ai_community.document_loaders.apify_dataset",
    "ArcGISLoader": "aibaba_ai_community.document_loaders.arcgis_loader",
    "ArxivLoader": "aibaba_ai_community.document_loaders.arxiv",
    "AssemblyAIAudioLoaderById": "aibaba_ai_community.document_loaders.assemblyai",
    "AssemblyAIAudioTranscriptLoader": "aibaba_ai_community.document_loaders.assemblyai",  # noqa: E501
    "AstraDBLoader": "aibaba_ai_community.document_loaders.astradb",
    "AsyncChromiumLoader": "aibaba_ai_community.document_loaders.chromium",
    "AsyncHtmlLoader": "aibaba_ai_community.document_loaders.async_html",
    "AthenaLoader": "aibaba_ai_community.document_loaders.athena",
    "AzureAIDataLoader": "aibaba_ai_community.document_loaders.azure_ai_data",
    "AzureAIDocumentIntelligenceLoader": "aibaba_ai_community.document_loaders.doc_intelligence",  # noqa: E501
    "AzureBlobStorageContainerLoader": "aibaba_ai_community.document_loaders.azure_blob_storage_container",  # noqa: E501
    "AzureBlobStorageFileLoader": "aibaba_ai_community.document_loaders.azure_blob_storage_file",  # noqa: E501
    "BSHTMLLoader": "aibaba_ai_community.document_loaders.html_bs",
    "BibtexLoader": "aibaba_ai_community.document_loaders.bibtex",
    "BigQueryLoader": "aibaba_ai_community.document_loaders.bigquery",
    "BiliBiliLoader": "aibaba_ai_community.document_loaders.bilibili",
    "BlackboardLoader": "aibaba_ai_community.document_loaders.blackboard",
    "Blob": "aibaba_ai_community.document_loaders.blob_loaders",
    "BlobLoader": "aibaba_ai_community.document_loaders.blob_loaders",
    "BlockchainDocumentLoader": "aibaba_ai_community.document_loaders.blockchain",
    "BraveSearchLoader": "aibaba_ai_community.document_loaders.brave_search",
    "BrowserbaseLoader": "aibaba_ai_community.document_loaders.browserbase",
    "BrowserlessLoader": "aibaba_ai_community.document_loaders.browserless",
    "CSVLoader": "aibaba_ai_community.document_loaders.csv_loader",
    "CassandraLoader": "aibaba_ai_community.document_loaders.cassandra",
    "ChatGPTLoader": "aibaba_ai_community.document_loaders.chatgpt",
    "CloudBlobLoader": "aibaba_ai_community.document_loaders.blob_loaders",
    "CoNLLULoader": "aibaba_ai_community.document_loaders.conllu",
    "CollegeConfidentialLoader": "aibaba_ai_community.document_loaders.college_confidential",  # noqa: E501
    "ConcurrentLoader": "aibaba_ai_community.document_loaders.concurrent",
    "ConfluenceLoader": "aibaba_ai_community.document_loaders.confluence",
    "CouchbaseLoader": "aibaba_ai_community.document_loaders.couchbase",
    "CubeSemanticLoader": "aibaba_ai_community.document_loaders.cube_semantic",
    "DataFrameLoader": "aibaba_ai_community.document_loaders.dataframe",
    "DatadogLogsLoader": "aibaba_ai_community.document_loaders.datadog_logs",
    "DedocAPIFileLoader": "aibaba_ai_community.document_loaders.dedoc",
    "DedocFileLoader": "aibaba_ai_community.document_loaders.dedoc",
    "DedocPDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "DiffbotLoader": "aibaba_ai_community.document_loaders.diffbot",
    "DirectoryLoader": "aibaba_ai_community.document_loaders.directory",
    "DiscordChatLoader": "aibaba_ai_community.document_loaders.discord",
    "DocugamiLoader": "aibaba_ai_community.document_loaders.docugami",
    "DocusaurusLoader": "aibaba_ai_community.document_loaders.docusaurus",
    "Docx2txtLoader": "aibaba_ai_community.document_loaders.word_document",
    "DropboxLoader": "aibaba_ai_community.document_loaders.dropbox",
    "DuckDBLoader": "aibaba_ai_community.document_loaders.duckdb_loader",
    "EtherscanLoader": "aibaba_ai_community.document_loaders.etherscan",
    "EverNoteLoader": "aibaba_ai_community.document_loaders.evernote",
    "FacebookChatLoader": "aibaba_ai_community.document_loaders.facebook_chat",
    "FaunaLoader": "aibaba_ai_community.document_loaders.fauna",
    "FigmaFileLoader": "aibaba_ai_community.document_loaders.figma",
    "FireCrawlLoader": "aibaba_ai_community.document_loaders.firecrawl",
    "FileSystemBlobLoader": "aibaba_ai_community.document_loaders.blob_loaders",
    "GCSDirectoryLoader": "aibaba_ai_community.document_loaders.gcs_directory",
    "GCSFileLoader": "aibaba_ai_community.document_loaders.gcs_file",
    "GeoDataFrameLoader": "aibaba_ai_community.document_loaders.geodataframe",
    "GitHubIssuesLoader": "aibaba_ai_community.document_loaders.github",
    "GitLoader": "aibaba_ai_community.document_loaders.git",
    "GitbookLoader": "aibaba_ai_community.document_loaders.gitbook",
    "GithubFileLoader": "aibaba_ai_community.document_loaders.github",
    "GlueCatalogLoader": "aibaba_ai_community.document_loaders.glue_catalog",
    "GoogleApiClient": "aibaba_ai_community.document_loaders.youtube",
    "GoogleApiYoutubeLoader": "aibaba_ai_community.document_loaders.youtube",
    "GoogleDriveLoader": "aibaba_ai_community.document_loaders.googledrive",
    "GoogleSpeechToTextLoader": "aibaba_ai_community.document_loaders.google_speech_to_text",  # noqa: E501
    "GutenbergLoader": "aibaba_ai_community.document_loaders.gutenberg",
    "HNLoader": "aibaba_ai_community.document_loaders.hn",
    "HuggingFaceDatasetLoader": "aibaba_ai_community.document_loaders.hugging_face_dataset",  # noqa: E501
    "HuggingFaceModelLoader": "aibaba_ai_community.document_loaders.hugging_face_model",
    "IFixitLoader": "aibaba_ai_community.document_loaders.ifixit",
    "IMSDbLoader": "aibaba_ai_community.document_loaders.imsdb",
    "ImageCaptionLoader": "aibaba_ai_community.document_loaders.image_captions",
    "IuguLoader": "aibaba_ai_community.document_loaders.iugu",
    "JSONLoader": "aibaba_ai_community.document_loaders.json_loader",
    "JoplinLoader": "aibaba_ai_community.document_loaders.joplin",
    "KineticaLoader": "aibaba_ai_community.document_loaders.kinetica_loader",
    "LakeFSLoader": "aibaba_ai_community.document_loaders.lakefs",
    "LarkSuiteDocLoader": "aibaba_ai_community.document_loaders.larksuite",
    "LLMSherpaFileLoader": "aibaba_ai_community.document_loaders.llmsherpa",
    "MHTMLLoader": "aibaba_ai_community.document_loaders.mhtml",
    "MWDumpLoader": "aibaba_ai_community.document_loaders.mediawikidump",
    "MastodonTootsLoader": "aibaba_ai_community.document_loaders.mastodon",
    "MathpixPDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "MaxComputeLoader": "aibaba_ai_community.document_loaders.max_compute",
    "MergedDataLoader": "aibaba_ai_community.document_loaders.merge",
    "ModernTreasuryLoader": "aibaba_ai_community.document_loaders.modern_treasury",
    "MongodbLoader": "aibaba_ai_community.document_loaders.mongodb",
    "NeedleLoader": "aibaba_ai_community.document_loaders.needle",
    "NewsURLLoader": "aibaba_ai_community.document_loaders.news",
    "NotebookLoader": "aibaba_ai_community.document_loaders.notebook",
    "NotionDBLoader": "aibaba_ai_community.document_loaders.notiondb",
    "NotionDirectoryLoader": "aibaba_ai_community.document_loaders.notion",
    "OBSDirectoryLoader": "aibaba_ai_community.document_loaders.obs_directory",
    "OBSFileLoader": "aibaba_ai_community.document_loaders.obs_file",
    "ObsidianLoader": "aibaba_ai_community.document_loaders.obsidian",
    "OneDriveFileLoader": "aibaba_ai_community.document_loaders.onedrive_file",
    "OneDriveLoader": "aibaba_ai_community.document_loaders.onedrive",
    "OnlinePDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "OpenCityDataLoader": "aibaba_ai_community.document_loaders.open_city_data",
    "OracleAutonomousDatabaseLoader": "aibaba_ai_community.document_loaders.oracleadb_loader",  # noqa: E501
    "OracleDocLoader": "aibaba_ai_community.document_loaders.oracleai",
    "OracleTextSplitter": "aibaba_ai_community.document_loaders.oracleai",
    "OutlookMessageLoader": "aibaba_ai_community.document_loaders.email",
    "PDFMinerLoader": "aibaba_ai_community.document_loaders.pdf",
    "PDFMinerPDFasHTMLLoader": "aibaba_ai_community.document_loaders.pdf",
    "PDFPlumberLoader": "aibaba_ai_community.document_loaders.pdf",
    "PagedPDFSplitter": "aibaba_ai_community.document_loaders.pdf",
    "PebbloSafeLoader": "aibaba_ai_community.document_loaders.pebblo",
    "PebbloTextLoader": "aibaba_ai_community.document_loaders.pebblo",
    "PlaywrightURLLoader": "aibaba_ai_community.document_loaders.url_playwright",
    "PolarsDataFrameLoader": "aibaba_ai_community.document_loaders.polars_dataframe",
    "PsychicLoader": "aibaba_ai_community.document_loaders.psychic",
    "PubMedLoader": "aibaba_ai_community.document_loaders.pubmed",
    "PyMuPDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "PyPDFDirectoryLoader": "aibaba_ai_community.document_loaders.pdf",
    "PyPDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "PyPDFium2Loader": "aibaba_ai_community.document_loaders.pdf",
    "PySparkDataFrameLoader": "aibaba_ai_community.document_loaders.pyspark_dataframe",
    "PythonLoader": "aibaba_ai_community.document_loaders.python",
    "RSSFeedLoader": "aibaba_ai_community.document_loaders.rss",
    "ReadTheDocsLoader": "aibaba_ai_community.document_loaders.readthedocs",
    "RecursiveUrlLoader": "aibaba_ai_community.document_loaders.recursive_url_loader",
    "RedditPostsLoader": "aibaba_ai_community.document_loaders.reddit",
    "RoamLoader": "aibaba_ai_community.document_loaders.roam",
    "RocksetLoader": "aibaba_ai_community.document_loaders.rocksetdb",
    "S3DirectoryLoader": "aibaba_ai_community.document_loaders.s3_directory",
    "S3FileLoader": "aibaba_ai_community.document_loaders.s3_file",
    "ScrapflyLoader": "aibaba_ai_community.document_loaders.scrapfly",
    "ScrapingAntLoader": "aibaba_ai_community.document_loaders.scrapingant",
    "SQLDatabaseLoader": "aibaba_ai_community.document_loaders.sql_database",
    "SRTLoader": "aibaba_ai_community.document_loaders.srt",
    "SeleniumURLLoader": "aibaba_ai_community.document_loaders.url_selenium",
    "SharePointLoader": "aibaba_ai_community.document_loaders.sharepoint",
    "SitemapLoader": "aibaba_ai_community.document_loaders.sitemap",
    "SlackDirectoryLoader": "aibaba_ai_community.document_loaders.slack_directory",
    "SnowflakeLoader": "aibaba_ai_community.document_loaders.snowflake_loader",
    "SpiderLoader": "aibaba_ai_community.document_loaders.spider",
    "SpreedlyLoader": "aibaba_ai_community.document_loaders.spreedly",
    "StripeLoader": "aibaba_ai_community.document_loaders.stripe",
    "SurrealDBLoader": "aibaba_ai_community.document_loaders.surrealdb",
    "TelegramChatApiLoader": "aibaba_ai_community.document_loaders.telegram",
    "TelegramChatFileLoader": "aibaba_ai_community.document_loaders.telegram",
    "TelegramChatLoader": "aibaba_ai_community.document_loaders.telegram",
    "TencentCOSDirectoryLoader": "aibaba_ai_community.document_loaders.tencent_cos_directory",  # noqa: E501
    "TencentCOSFileLoader": "aibaba_ai_community.document_loaders.tencent_cos_file",
    "TensorflowDatasetLoader": "aibaba_ai_community.document_loaders.tensorflow_datasets",  # noqa: E501
    "TextLoader": "aibaba_ai_community.document_loaders.text",
    "TiDBLoader": "aibaba_ai_community.document_loaders.tidb",
    "ToMarkdownLoader": "aibaba_ai_community.document_loaders.tomarkdown",
    "TomlLoader": "aibaba_ai_community.document_loaders.toml",
    "TrelloLoader": "aibaba_ai_community.document_loaders.trello",
    "TwitterTweetLoader": "aibaba_ai_community.document_loaders.twitter",
    "UnstructuredAPIFileIOLoader": "aibaba_ai_community.document_loaders.unstructured",
    "UnstructuredAPIFileLoader": "aibaba_ai_community.document_loaders.unstructured",
    "UnstructuredCHMLoader": "aibaba_ai_community.document_loaders.chm",
    "UnstructuredCSVLoader": "aibaba_ai_community.document_loaders.csv_loader",
    "UnstructuredEPubLoader": "aibaba_ai_community.document_loaders.epub",
    "UnstructuredEmailLoader": "aibaba_ai_community.document_loaders.email",
    "UnstructuredExcelLoader": "aibaba_ai_community.document_loaders.excel",
    "UnstructuredFileIOLoader": "aibaba_ai_community.document_loaders.unstructured",
    "UnstructuredFileLoader": "aibaba_ai_community.document_loaders.unstructured",
    "UnstructuredHTMLLoader": "aibaba_ai_community.document_loaders.html",
    "UnstructuredImageLoader": "aibaba_ai_community.document_loaders.image",
    "UnstructuredMarkdownLoader": "aibaba_ai_community.document_loaders.markdown",
    "UnstructuredODTLoader": "aibaba_ai_community.document_loaders.odt",
    "UnstructuredOrgModeLoader": "aibaba_ai_community.document_loaders.org_mode",
    "UnstructuredPDFLoader": "aibaba_ai_community.document_loaders.pdf",
    "UnstructuredPowerPointLoader": "aibaba_ai_community.document_loaders.powerpoint",
    "UnstructuredRSTLoader": "aibaba_ai_community.document_loaders.rst",
    "UnstructuredRTFLoader": "aibaba_ai_community.document_loaders.rtf",
    "UnstructuredTSVLoader": "aibaba_ai_community.document_loaders.tsv",
    "UnstructuredURLLoader": "aibaba_ai_community.document_loaders.url",
    "UnstructuredWordDocumentLoader": "aibaba_ai_community.document_loaders.word_document",  # noqa: E501
    "UnstructuredXMLLoader": "aibaba_ai_community.document_loaders.xml",
    "VsdxLoader": "aibaba_ai_community.document_loaders.vsdx",
    "WeatherDataLoader": "aibaba_ai_community.document_loaders.weather",
    "WebBaseLoader": "aibaba_ai_community.document_loaders.web_base",
    "WhatsAppChatLoader": "aibaba_ai_community.document_loaders.whatsapp_chat",
    "WikipediaLoader": "aibaba_ai_community.document_loaders.wikipedia",
    "XorbitsLoader": "aibaba_ai_community.document_loaders.xorbits",
    "YoutubeAudioLoader": "aibaba_ai_community.document_loaders.blob_loaders",
    "YoutubeLoader": "aibaba_ai_community.document_loaders.youtube",
    "YuqueLoader": "aibaba_ai_community.document_loaders.yuque",
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "AZLyricsLoader",
    "AcreomLoader",
    "AirbyteCDKLoader",
    "AirbyteGongLoader",
    "AirbyteHubspotLoader",
    "AirbyteJSONLoader",
    "AirbyteSalesforceLoader",
    "AirbyteShopifyLoader",
    "AirbyteStripeLoader",
    "AirbyteTypeformLoader",
    "AirbyteZendeskSupportLoader",
    "AirtableLoader",
    "AmazonTextractPDFLoader",
    "ApifyDatasetLoader",
    "ArcGISLoader",
    "ArxivLoader",
    "AssemblyAIAudioLoaderById",
    "AssemblyAIAudioTranscriptLoader",
    "AstraDBLoader",
    "AsyncChromiumLoader",
    "AsyncHtmlLoader",
    "AthenaLoader",
    "AzureAIDataLoader",
    "AzureAIDocumentIntelligenceLoader",
    "AzureBlobStorageContainerLoader",
    "AzureBlobStorageFileLoader",
    "BSHTMLLoader",
    "BibtexLoader",
    "BigQueryLoader",
    "BiliBiliLoader",
    "BlackboardLoader",
    "Blob",
    "BlobLoader",
    "BlockchainDocumentLoader",
    "BraveSearchLoader",
    "BrowserbaseLoader",
    "BrowserlessLoader",
    "CSVLoader",
    "CassandraLoader",
    "ChatGPTLoader",
    "CloudBlobLoader",
    "CoNLLULoader",
    "CollegeConfidentialLoader",
    "ConcurrentLoader",
    "ConfluenceLoader",
    "CouchbaseLoader",
    "CubeSemanticLoader",
    "DataFrameLoader",
    "DatadogLogsLoader",
    "DedocAPIFileLoader",
    "DedocFileLoader",
    "DedocPDFLoader",
    "DiffbotLoader",
    "DirectoryLoader",
    "DiscordChatLoader",
    "DocugamiLoader",
    "DocusaurusLoader",
    "Docx2txtLoader",
    "DropboxLoader",
    "DuckDBLoader",
    "EtherscanLoader",
    "EverNoteLoader",
    "FacebookChatLoader",
    "FaunaLoader",
    "FigmaFileLoader",
    "FireCrawlLoader",
    "FileSystemBlobLoader",
    "GCSDirectoryLoader",
    "GlueCatalogLoader",
    "GCSFileLoader",
    "GeoDataFrameLoader",
    "GitHubIssuesLoader",
    "GitLoader",
    "GitbookLoader",
    "GithubFileLoader",
    "GoogleApiClient",
    "GoogleApiYoutubeLoader",
    "GoogleDriveLoader",
    "GoogleSpeechToTextLoader",
    "GutenbergLoader",
    "HNLoader",
    "HuggingFaceDatasetLoader",
    "HuggingFaceModelLoader",
    "IFixitLoader",
    "ImageCaptionLoader",
    "IMSDbLoader",
    "IuguLoader",
    "JoplinLoader",
    "JSONLoader",
    "KineticaLoader",
    "LakeFSLoader",
    "LarkSuiteDocLoader",
    "LLMSherpaFileLoader",
    "MastodonTootsLoader",
    "MHTMLLoader",
    "MWDumpLoader",
    "MathpixPDFLoader",
    "MaxComputeLoader",
    "MergedDataLoader",
    "ModernTreasuryLoader",
    "MongodbLoader",
    "NeedleLoader",
    "NewsURLLoader",
    "NotebookLoader",
    "NotionDBLoader",
    "NotionDirectoryLoader",
    "OBSDirectoryLoader",
    "OBSFileLoader",
    "ObsidianLoader",
    "OneDriveFileLoader",
    "OneDriveLoader",
    "OnlinePDFLoader",
    "OpenCityDataLoader",
    "OracleAutonomousDatabaseLoader",
    "OracleDocLoader",
    "OracleTextSplitter",
    "OutlookMessageLoader",
    "PDFMinerLoader",
    "PDFMinerPDFasHTMLLoader",
    "PDFPlumberLoader",
    "PagedPDFSplitter",
    "PebbloSafeLoader",
    "PebbloTextLoader",
    "PlaywrightURLLoader",
    "PolarsDataFrameLoader",
    "PsychicLoader",
    "PubMedLoader",
    "PyMuPDFLoader",
    "PyPDFDirectoryLoader",
    "PyPDFLoader",
    "PyPDFium2Loader",
    "PySparkDataFrameLoader",
    "PythonLoader",
    "RSSFeedLoader",
    "ReadTheDocsLoader",
    "RecursiveUrlLoader",
    "RedditPostsLoader",
    "RoamLoader",
    "RocksetLoader",
    "S3DirectoryLoader",
    "S3FileLoader",
    "ScrapflyLoader",
    "ScrapingAntLoader",
    "SQLDatabaseLoader",
    "SRTLoader",
    "SeleniumURLLoader",
    "SharePointLoader",
    "SitemapLoader",
    "SlackDirectoryLoader",
    "SnowflakeLoader",
    "SpiderLoader",
    "SpreedlyLoader",
    "StripeLoader",
    "SurrealDBLoader",
    "TelegramChatApiLoader",
    "TelegramChatFileLoader",
    "TelegramChatLoader",
    "TencentCOSDirectoryLoader",
    "TencentCOSFileLoader",
    "TensorflowDatasetLoader",
    "TextLoader",
    "TiDBLoader",
    "ToMarkdownLoader",
    "TomlLoader",
    "TrelloLoader",
    "TwitterTweetLoader",
    "UnstructuredAPIFileIOLoader",
    "UnstructuredAPIFileLoader",
    "UnstructuredCHMLoader",
    "UnstructuredCSVLoader",
    "UnstructuredEPubLoader",
    "UnstructuredEmailLoader",
    "UnstructuredExcelLoader",
    "UnstructuredFileIOLoader",
    "UnstructuredFileLoader",
    "UnstructuredHTMLLoader",
    "UnstructuredImageLoader",
    "UnstructuredMarkdownLoader",
    "UnstructuredODTLoader",
    "UnstructuredOrgModeLoader",
    "UnstructuredPDFLoader",
    "UnstructuredPowerPointLoader",
    "UnstructuredRSTLoader",
    "UnstructuredRTFLoader",
    "UnstructuredTSVLoader",
    "UnstructuredURLLoader",
    "UnstructuredWordDocumentLoader",
    "UnstructuredXMLLoader",
    "VsdxLoader",
    "WeatherDataLoader",
    "WebBaseLoader",
    "WhatsAppChatLoader",
    "WikipediaLoader",
    "XorbitsLoader",
    "YoutubeAudioLoader",
    "YoutubeLoader",
    "YuqueLoader",
]
