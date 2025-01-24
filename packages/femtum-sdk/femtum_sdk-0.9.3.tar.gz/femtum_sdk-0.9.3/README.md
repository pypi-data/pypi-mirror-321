# Femtum SDK - Python

[![NuGet](https://img.shields.io/nuget/v/Femtum.SDK.svg)](https://www.nuget.org/packages/Femtum.SDK)

### Installation

To install the Femtum SDK, use the following command:

##### pip

```bash
pip install femtum-sdk
```

##### poetry

```bash
poetry add femtum-sdk
```

### Usage

Here is a basic example of how to use the Femtum SDK:

1. Start the SDK Server
2. Use SDK in your code

```python
from femtum_sdk.adapter.analysis_pandas_adapter import SweepResulToDataframe
from femtum_sdk.core.analysis_pb2 import (
    FindResultByIdRequest,
    ListByPageResultsRequest,
    OptionalSweepResult,
    ResultsFilterRequest,
    ResultsPage,
)

from femtum_sdk import FemtumSdk

with FemtumSdk() as sdk:
    page: ResultsPage = sdk.analysis.ListByPageResults(
        ListByPageResultsRequest(
            PageSize=10,
            PageNumber=1,
            Filters=ResultsFilterRequest(
                WaferName="FITZY005",
                ReticleName="R20",
                DieName="MZI",
                CircuitName="ICR3_GC_MZITEw300nmL100um",
            ),
        )
    )

    firstResultWithData: OptionalSweepResult = sdk.analysis.FindSweepResultById(
        FindResultByIdRequest(Id=page.Items[0].Id)
    )

    print(firstResultWithData.Result.WavelengthsArray)
    print(firstResultWithData.Result.WavelengthsArray)
    print(firstResultWithData.Result.PowersArray)

    dataframe = SweepResulToDataframe(firstResultWithData.Result)
    print(dataframe)
```

#### With Specified SDK server url

```python
with FemtumSdk(hostUrl=api_server.get_grpc_url()) as sdk:
  request = FindResultDataRequestDto()
  result: OpticalSpectralAnalyserSweepResultArray = (
      sdk.analysis.FindOpticalSpectralAnalyserSweepResults(request)
  )

  print(result.Items)
```
