from deepcrawl_graphql.api import DeepCrawlConnection
from deepcrawl_graphql.reports.fields import ReportDownloadFields


class ReportDownloadMutation:
    def __init__(self, conn: DeepCrawlConnection) -> None:
        self.conn = conn
        self.ds = conn.ds
        self.mutation = self.ds.Mutation

    def create_report_download(self, report_download_input, fields=None):
        """Creates a report download.

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input CreateReportDownloadInput {
                  crawlAccessibilityIssueFilter: CrawlAccessibilityIssueConnectionFilterInput
                  crawlAccessibilityIssueInstanceFilter: CrawlAccessibilityIssueInstanceConnectionFilterInput
                  crawlDuplicateUrlFilter: CrawlDuplicateUrlConnectionFilterInput
                  crawlHreflangsFilter: CrawlHreflangsConnectionFilterInput
                  crawlId: ObjectID
                  crawlLinkFilter: CrawlLinkConnectionFilterInput
                  crawlLinkedDomainFilter: CrawlLinkedDomainConnectionFilterInput
                  crawlOriginFilter: CrawlOriginConnectionFilterInput
                  crawlSearchQueryFilter: CrawlSearchQueryConnectionFilterInput
                  crawlSearchQueryWithLandingPagesFilter: CrawlSearchQueryWithLandingPagesConnectionFilterInput
                  crawlSiteSpeedAuditFilter: CrawlSiteSpeedAuditConnectionFilterInput
                  crawlSiteSpeedAuditItemFilter: CrawlSiteSpeedAuditItemConnectionFilterInput
                  crawlSiteSpeedAuditOpportunityFilter: CrawlSiteSpeedAuditOpportunityConnectionFilterInput
                  crawlSitemapFilter: CrawlSitemapConnectionFilterInput
                  crawlUncrawledUrlFilter: CrawlUncrawledUrlConnectionFilterInput
                  crawlUniqueLinkFilter: CrawlUniqueLinkConnectionFilterInput
                  crawlUrlFilter: CrawlUrlConnectionFilterInput
                  crawlWebCrawlDepthFilter: CrawlWebCrawlDepthConnectionFilterInput
                  fileName: String
                  filter: JSONObject
                  outputType: ReportDownloadOutputType! = CsvZip
                  reportId: ObjectID @deprecated(reason: "Use combination of crawlId, reportTemplateCode and reportTypeCode instead, with optional segmentId.")
                  reportTemplateCode: String
                  reportTypeCode: ReportTypeCode
                  segmentId: ObjectID
                  selectedMetrics: [String!]
                }

        :param report_download_input: Report Download input.
        :type report_download_input: dict
        :param fields: Select specific fields.
        :type fields: List(DSLField)
        """
        mutation = self.mutation.createReportDownload.args(
            input=report_download_input
        ).select(
            self.ds.CreateReportDownloadPayload.reportDownload.select(
                *fields or ReportDownloadFields.fields(self.ds)
            )
        )
        return self.conn.run_mutation(mutation)

    def delete_report_download(self, report_download_id, fields=None):
        """Deletes a report download.

        :param report_download_id: Report Download id.
        :type report_download_id: int or str
        :param fields: Select specific fields.
        :type fields: List(DSLField)
        """
        mutation = self.mutation.deleteReportDownload.args(
            input={"reportDownloadId": report_download_id}
        ).select(
            self.ds.DeleteReportDownloadPayload.reportDownload.select(
                *fields or ReportDownloadFields.fields(self.ds)
            )
        )
        return self.conn.run_mutation(mutation)
