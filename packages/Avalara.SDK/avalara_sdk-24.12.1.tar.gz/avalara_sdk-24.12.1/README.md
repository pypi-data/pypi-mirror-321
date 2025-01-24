# Avalara.SDK - the Unified Java SDK for next gen Avalara services.

Unified SDK consists of services on top of which the Avalara Compliance Cloud platform is built. These services are foundational and provide functionality such as einvoicing.

## Requirements.

Python >= 3.6

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import Avalara.SDK
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import Avalara.SDK
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import Avalara.SDK
from Avalara.SDK import api_client
from Avalara.SDK.api.EInvoicing.V1.mandates_api import MandatesApi  # noqa: E501
from pprint import pprint

# Define configuration object with parameters specified to your application.
configuration = Avalara.SDK.Configuration(
    app_name='test app'
    app_version='1.0'
    machine_name='some machine'
    access_token='YOUR_BEARER_TOKEN'
    environment='sandbox'
)
# Enter a context with an instance of the API client
with Avalara.SDK.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MandatesApi(api_client)
    x_avalara_client = "Swagger UI; 22.7.0; Custom; 1.0" # str | Identifies the software you are using to call this API.  For more information on the client header, see [Client Headers](https://developer.avalara.com/avatax/client-headers/) . (optional) if omitted the server will use the default value of "Swagger UI; 22.7.0; Custom; 1.0"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve geolocation information for a specified address
        api_response = api_instance.get_mandates(avalara_version="1.2", x_avalara_client=x_avalara_client)
        pprint(api_response)
    except Avalara.SDK.ApiException as e:
        print("Exception when calling MandatesApi->get_mandates: %s\n" % e)
```

## Documentation for API Endpoints

<a name="documentation-for-EInvoicing-V1-api-endpoints"></a>

### EInvoicing V1 API Documentation

| Class                | Method                                                                                                    | HTTP request                                                    | Description                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| _DataInputFieldsApi_ | [**get_data_input_fields**](docs/EInvoicing/V1/DataInputFieldsApi.md#get_data_input_fields)               | **GET** /data-input-fields                                      | Returns the optionality of document fields for different country mandates                               |
| _DocumentsApi_       | [**download_document**](docs/EInvoicing/V1/DocumentsApi.md#download_document)                             | **GET** /documents/{documentId}/$download                       | Returns a copy of the document                                                                          |
| _DocumentsApi_       | [**fetch_documents**](docs/EInvoicing/V1/DocumentsApi.md#fetch_documents)                                 | **POST** /documents/$fetch                                      | Fetch the inbound document from a tax authority                                                         |
| _DocumentsApi_       | [**get_document_list**](docs/EInvoicing/V1/DocumentsApi.md#get_document_list)                             | **GET** /documents                                              | Returns a summary of documents for a date range                                                         |
| _DocumentsApi_       | [**get_document_status**](docs/EInvoicing/V1/DocumentsApi.md#get_document_status)                         | **GET** /documents/{documentId}/status                          | Checks the status of a document                                                                         |
| _DocumentsApi_       | [**submit_document**](docs/EInvoicing/V1/DocumentsApi.md#submit_document)                                 | **POST** /documents                                             | Submits a document to Avalara E-Invoicing API                                                           |
| _InteropApi_         | [**submit_interop_document**](docs/EInvoicing/V1/InteropApi.md#submit_interop_document)                   | **POST** /interop/documents                                     | Submit a document                                                                                       |
| _MandatesApi_        | [**get_mandate_data_input_fields**](docs/EInvoicing/V1/MandatesApi.md#get_mandate_data_input_fields)      | **GET** /mandates/{mandateId}/data-input-fields                 | Returns document field information for a country mandate, a selected document type, and its version     |
| _MandatesApi_        | [**get_mandates**](docs/EInvoicing/V1/MandatesApi.md#get_mandates)                                        | **GET** /mandates                                               | List country mandates that are supported by the Avalara E-Invoicing platform                            |
| _TradingPartnersApi_ | [**batch_search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#batch_search_participants)       | **POST** /trading-partners/batch-searches                       | Creates a batch search and performs a batch search in the directory for participants in the background. |
| _TradingPartnersApi_ | [**download_batch_search_report**](docs/EInvoicing/V1/TradingPartnersApi.md#download_batch_search_report) | **GET** /trading-partners/batch-searches/{id}/$download-results | Download batch search results in a csv file.                                                            |
| _TradingPartnersApi_ | [**get_batch_search_detail**](docs/EInvoicing/V1/TradingPartnersApi.md#get_batch_search_detail)           | **GET** /trading-partners/batch-searches/{id}                   | Get the batch search details for a given id.                                                            |
| _TradingPartnersApi_ | [**list_batch_searches**](docs/EInvoicing/V1/TradingPartnersApi.md#list_batch_searches)                   | **GET** /trading-partners/batch-searches                        | List all batch searches that were previously submitted.                                                 |
| _TradingPartnersApi_ | [**search_participants**](docs/EInvoicing/V1/TradingPartnersApi.md#search_participants)                   | **GET** /trading-partners                                       | Returns a list of participants matching the input query.                                                |

<a name="documentation-for-models"></a>

## Documentation for Models

<a name="documentation-for-EInvoicing-V1-models"></a>

### EInvoicing V1 Model Documentation

- [Avalara.SDK.models.EInvoicing.V1.BadDownloadRequest](docs/EInvoicing/V1/BadDownloadRequest.md)
- [Avalara.SDK.models.EInvoicing.V1.BadRequest](docs/EInvoicing/V1/BadRequest.md)
- [Avalara.SDK.models.EInvoicing.V1.BatchSearch](docs/EInvoicing/V1/BatchSearch.md)
- [Avalara.SDK.models.EInvoicing.V1.BatchSearchListResponse](docs/EInvoicing/V1/BatchSearchListResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.ConditionalForField](docs/EInvoicing/V1/ConditionalForField.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputField](docs/EInvoicing/V1/DataInputField.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldNotUsedFor](docs/EInvoicing/V1/DataInputFieldNotUsedFor.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldOptionalFor](docs/EInvoicing/V1/DataInputFieldOptionalFor.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldRequiredFor](docs/EInvoicing/V1/DataInputFieldRequiredFor.md)
- [Avalara.SDK.models.EInvoicing.V1.DataInputFieldsResponse](docs/EInvoicing/V1/DataInputFieldsResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponse](docs/EInvoicing/V1/DirectorySearchResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInner](docs/EInvoicing/V1/DirectorySearchResponseValueInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerAddressesInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerAddressesInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerIdentifiersInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerIdentifiersInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DirectorySearchResponseValueInnerSupportedDocumentTypesInner](docs/EInvoicing/V1/DirectorySearchResponseValueInnerSupportedDocumentTypesInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetch](docs/EInvoicing/V1/DocumentFetch.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetchRequest](docs/EInvoicing/V1/DocumentFetchRequest.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetchRequestDataInner](docs/EInvoicing/V1/DocumentFetchRequestDataInner.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentFetchRequestMetadata](docs/EInvoicing/V1/DocumentFetchRequestMetadata.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentListResponse](docs/EInvoicing/V1/DocumentListResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentStatusResponse](docs/EInvoicing/V1/DocumentStatusResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentSubmissionError](docs/EInvoicing/V1/DocumentSubmissionError.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentSubmitResponse](docs/EInvoicing/V1/DocumentSubmitResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.DocumentSummary](docs/EInvoicing/V1/DocumentSummary.md)
- [Avalara.SDK.models.EInvoicing.V1.ErrorResponse](docs/EInvoicing/V1/ErrorResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.ForbiddenError](docs/EInvoicing/V1/ForbiddenError.md)
- [Avalara.SDK.models.EInvoicing.V1.InputDataFormats](docs/EInvoicing/V1/InputDataFormats.md)
- [Avalara.SDK.models.EInvoicing.V1.InternalServerError](docs/EInvoicing/V1/InternalServerError.md)
- [Avalara.SDK.models.EInvoicing.V1.Mandate](docs/EInvoicing/V1/Mandate.md)
- [Avalara.SDK.models.EInvoicing.V1.MandateDataInputField](docs/EInvoicing/V1/MandateDataInputField.md)
- [Avalara.SDK.models.EInvoicing.V1.MandateDataInputFieldNamespace](docs/EInvoicing/V1/MandateDataInputFieldNamespace.md)
- [Avalara.SDK.models.EInvoicing.V1.MandatesResponse](docs/EInvoicing/V1/MandatesResponse.md)
- [Avalara.SDK.models.EInvoicing.V1.NotFoundError](docs/EInvoicing/V1/NotFoundError.md)
- [Avalara.SDK.models.EInvoicing.V1.NotUsedForField](docs/EInvoicing/V1/NotUsedForField.md)
- [Avalara.SDK.models.EInvoicing.V1.RequiredWhenField](docs/EInvoicing/V1/RequiredWhenField.md)
- [Avalara.SDK.models.EInvoicing.V1.StatusEvent](docs/EInvoicing/V1/StatusEvent.md)
- [Avalara.SDK.models.EInvoicing.V1.SubmitDocumentMetadata](docs/EInvoicing/V1/SubmitDocumentMetadata.md)
- [Avalara.SDK.models.EInvoicing.V1.SubmitInteropDocument202Response](docs/EInvoicing/V1/SubmitInteropDocument202Response.md)
- [Avalara.SDK.models.EInvoicing.V1.WorkflowIds](docs/EInvoicing/V1/WorkflowIds.md)
