"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from mixpeek import models, utils
from mixpeek._hooks import HookContext
from mixpeek.types import OptionalNullable, UNSET
from mixpeek.utils import get_security_from_env
from typing import Any, List, Mapping, Optional, Union


class FeatureSearch(BaseSDK):
    def search_features_v1_features_search_post(
        self,
        *,
        collections: List[str],
        offset_position: OptionalNullable[int] = UNSET,
        page_size: Optional[int] = 10,
        x_namespace: OptionalNullable[str] = UNSET,
        queries: OptionalNullable[
            Union[
                List[models.SearchModelSearchQuery],
                List[models.SearchModelSearchQueryTypedDict],
            ]
        ] = UNSET,
        filters: OptionalNullable[
            Union[models.LogicalOperator, models.LogicalOperatorTypedDict]
        ] = UNSET,
        group_by: OptionalNullable[
            Union[models.GroupByOptions, models.GroupByOptionsTypedDict]
        ] = UNSET,
        sort: OptionalNullable[
            Union[models.SortOption, models.SortOptionTypedDict]
        ] = UNSET,
        select: OptionalNullable[List[str]] = UNSET,
        reranking_options: OptionalNullable[
            Union[models.RerankingOptions, models.RerankingOptionsTypedDict]
        ] = UNSET,
        session_id: OptionalNullable[str] = UNSET,
        return_url: OptionalNullable[bool] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPost:
        r"""Search Features

        This endpoint allows you to search features.

        :param collections: List of Collection names to search within, required
        :param offset_position: The position to start returning results from. Used for pagination. Does not work with group_by
        :param page_size: Number of results to return per page.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param queries: List of search queries to perform.                  Behavior:         - Single query: Results are returned directly from that query         - Multiple queries: Results are combined using Reciprocal Rank Fusion (RRF)                  RRF combines results from multiple queries by:         1. Taking each item's rank position in each result list         2. Re-ranking all items by their combined RRF scores                  When merging lists from different sources,          RRF considers all items that appear in any of the input lists,          not just items that appear in all lists.                  This helps surface items that rank well across multiple queries while         reducing the impact of outlier high rankings in single queries.                  NOTE: If query array is empty, it will return all features.
        :param filters: Used for filtering across all indexes
        :param group_by: Grouping options for search results
        :param sort: List of fields to sort by, with direction (asc or desc). Supports dot notation for nested fields.
        :param select: List of fields to return in results, supports dot notation. If None, all fields are returned.
        :param reranking_options: Options for ranking the search results, including weights and feedback application
        :param session_id: Identifier for tracking search session interactions
        :param return_url: Return the presigned URL for the asset and preview asset, this will introduce additional latency
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.SearchFeaturesV1FeaturesSearchPostRequest(
            offset_position=offset_position,
            page_size=page_size,
            x_namespace=x_namespace,
            search_request_features=models.SearchRequestFeatures(
                queries=utils.get_pydantic_model(
                    queries, OptionalNullable[List[models.SearchModelSearchQuery]]
                ),
                collections=collections,
                filters=utils.get_pydantic_model(
                    filters, OptionalNullable[models.LogicalOperator]
                ),
                group_by=utils.get_pydantic_model(
                    group_by, OptionalNullable[models.GroupByOptions]
                ),
                sort=utils.get_pydantic_model(
                    sort, OptionalNullable[models.SortOption]
                ),
                select=select,
                reranking_options=utils.get_pydantic_model(
                    reranking_options, OptionalNullable[models.RerankingOptions]
                ),
                session_id=session_id,
                return_url=return_url,
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/features/search",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.search_request_features,
                False,
                False,
                "json",
                models.SearchRequestFeatures,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="search_features_v1_features_search_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text,
                models.SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPost,
            )
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def search_features_v1_features_search_post_async(
        self,
        *,
        collections: List[str],
        offset_position: OptionalNullable[int] = UNSET,
        page_size: Optional[int] = 10,
        x_namespace: OptionalNullable[str] = UNSET,
        queries: OptionalNullable[
            Union[
                List[models.SearchModelSearchQuery],
                List[models.SearchModelSearchQueryTypedDict],
            ]
        ] = UNSET,
        filters: OptionalNullable[
            Union[models.LogicalOperator, models.LogicalOperatorTypedDict]
        ] = UNSET,
        group_by: OptionalNullable[
            Union[models.GroupByOptions, models.GroupByOptionsTypedDict]
        ] = UNSET,
        sort: OptionalNullable[
            Union[models.SortOption, models.SortOptionTypedDict]
        ] = UNSET,
        select: OptionalNullable[List[str]] = UNSET,
        reranking_options: OptionalNullable[
            Union[models.RerankingOptions, models.RerankingOptionsTypedDict]
        ] = UNSET,
        session_id: OptionalNullable[str] = UNSET,
        return_url: OptionalNullable[bool] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPost:
        r"""Search Features

        This endpoint allows you to search features.

        :param collections: List of Collection names to search within, required
        :param offset_position: The position to start returning results from. Used for pagination. Does not work with group_by
        :param page_size: Number of results to return per page.
        :param x_namespace: Optional namespace for data isolation. This can be a namespace name or namespace ID. Example: 'netflix_prod' or 'ns_1234567890'. To create a namespace, use the /namespaces endpoint.
        :param queries: List of search queries to perform.                  Behavior:         - Single query: Results are returned directly from that query         - Multiple queries: Results are combined using Reciprocal Rank Fusion (RRF)                  RRF combines results from multiple queries by:         1. Taking each item's rank position in each result list         2. Re-ranking all items by their combined RRF scores                  When merging lists from different sources,          RRF considers all items that appear in any of the input lists,          not just items that appear in all lists.                  This helps surface items that rank well across multiple queries while         reducing the impact of outlier high rankings in single queries.                  NOTE: If query array is empty, it will return all features.
        :param filters: Used for filtering across all indexes
        :param group_by: Grouping options for search results
        :param sort: List of fields to sort by, with direction (asc or desc). Supports dot notation for nested fields.
        :param select: List of fields to return in results, supports dot notation. If None, all fields are returned.
        :param reranking_options: Options for ranking the search results, including weights and feedback application
        :param session_id: Identifier for tracking search session interactions
        :param return_url: Return the presigned URL for the asset and preview asset, this will introduce additional latency
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.SearchFeaturesV1FeaturesSearchPostRequest(
            offset_position=offset_position,
            page_size=page_size,
            x_namespace=x_namespace,
            search_request_features=models.SearchRequestFeatures(
                queries=utils.get_pydantic_model(
                    queries, OptionalNullable[List[models.SearchModelSearchQuery]]
                ),
                collections=collections,
                filters=utils.get_pydantic_model(
                    filters, OptionalNullable[models.LogicalOperator]
                ),
                group_by=utils.get_pydantic_model(
                    group_by, OptionalNullable[models.GroupByOptions]
                ),
                sort=utils.get_pydantic_model(
                    sort, OptionalNullable[models.SortOption]
                ),
                select=select,
                reranking_options=utils.get_pydantic_model(
                    reranking_options, OptionalNullable[models.RerankingOptions]
                ),
                session_id=session_id,
                return_url=return_url,
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/features/search",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.search_request_features,
                False,
                False,
                "json",
                models.SearchRequestFeatures,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="search_features_v1_features_search_post",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["400", "401", "403", "404", "422", "4XX", "500", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text,
                models.SearchFeaturesV1FeaturesSearchPostResponseSearchFeaturesV1FeaturesSearchPost,
            )
        if utils.match_response(
            http_res, ["400", "401", "403", "404", "500"], "application/json"
        ):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
