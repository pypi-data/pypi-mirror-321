from deepcrawl_graphql.api import DeepCrawlConnection
from deepcrawl_graphql.projects.fields import ProjectFields


class ProjectMutation:
    def __init__(self, conn: DeepCrawlConnection) -> None:
        self.conn = conn
        self.ds = conn.ds
        self.mutation = self.ds.Mutation

    def create_project(self, project_input, fields=None):
        """Creates a Project

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input CreateProjectInput {
                  accountId: ObjectID!
                  alertEmails: [String!]
                  alertSettingCode: AlertSettingCode! = Always
                  apiCallbackHeaders: [APICallbackHeaderInput!]! = []
                  apiCallbackUrl: String = null
                  applyCustomHeadersToNavigationRequestsOnly: Boolean! = false
                  autoFinalizeOnCrawlLimits: Boolean! = true
                  block3rdPartyCookies: Boolean! = false
                  compareToCrawl: CompareToCrawlType! = LastCrawl
                  crawlDisallowedUrls1stLevel: Boolean! = false
                  crawlHyperlinksExternal: Boolean! = false
                  crawlHyperlinksInternal: Boolean! = true
                  crawlImagesExternal: Boolean! = false
                  crawlImagesInternal: Boolean! = false
                  crawlNofollowHyperlinks: Boolean! = true
                  crawlNonHtml: Boolean! = false
                  crawlNotIncluded1stLevel: Boolean! = false
                  crawlRedirectsExternal: Boolean! = true
                  crawlRedirectsInternal: Boolean! = true
                  crawlRelAmphtmlExternal: Boolean! = false
                  crawlRelAmphtmlInternal: Boolean! = true
                  crawlRelCanonicalsExternal: Boolean! = false
                  crawlRelCanonicalsInternal: Boolean! = true
                  crawlRelHreflangsExternal: Boolean! = false
                  crawlRelHreflangsInternal: Boolean! = true
                  crawlRelMobileExternal: Boolean! = false
                  crawlRelMobileInternal: Boolean! = true
                  crawlRelNextPrevExternal: Boolean! = false
                  crawlRelNextPrevInternal: Boolean! = true
                  crawlRobotsTxtNoindex: Boolean! = true
                  crawlScriptsExternal: Boolean! = true
                  crawlScriptsInternal: Boolean! = true
                  crawlStylesheetsExternal: Boolean! = true
                  crawlStylesheetsInternal: Boolean! = true
                  crawlTestSite: Boolean! = false
                  crawlTypes: [CrawlType!]! = [Web]
                  customDns: [CustomDnsSettingInput!]! = []
                  customExtractions: [CustomExtractionSettingInput!]! = []
                  customRequestHeaders: [CustomRequestHeaderInput!]! = []
                  dataLayerName: String = null
                  dataOnlyCrawlTypes: [CrawlType!]
                  discoverSitemapsInRobotsTxt: Boolean! = true
                  duplicatePrecision: Float! = 3
                  emptyPageThreshold: Int! = 512
                  enableKeyValueStore: Boolean! = false
                  excludeUrlPatterns: [String!]! = []
                  excludedDatasources: [DatasourceCode!]
                  failureRateLimitEnabled: Boolean! = false
                  failureRateLookbackWindow: Int! = 300
                  failureRateThreshold: Float! = 50
                  flattenIframes: Boolean! = false
                  flattenShadowDom: Boolean! = false
                  gaDateRange: Int! = 30
                  ignoreInvalidSSLCertificate: Boolean! = false
                  ignoreRobotsForNavigationRequests: Boolean! = false
                  includeBestPractices: Boolean! = true
                  includeHttpAndHttps: Boolean! = false
                  includeSubdomains: Boolean! = false
                  includeUrlPatterns: [String!]! = []
                  industryCode: String
                  limitLevelsMax: Int
                  limitUrlsMax: Int
                  locationCode: LocationCode! = Default
                  logSummaryRequestsHigh: Int! = 100
                  logSummaryRequestsLow: Int! = 10
                  maxBodyContentLength: Int! = 51200
                  maxDescriptionLength: Int! = 230
                  maxFollowedExternalLinks: Int! = 10
                  maxHtmlSize: Int! = 204800
                  maxLinks: Int! = 250
                  maxLoadTime: Float! = 3
                  maxRedirections: Int! = 4
                  maxTitleWidth: Int! = 600
                  maxUrlLength: Int! = 1024
                  maximumCrawlRate: Float! = 3
                  maximumCrawlRateAdvanced: [AdvancedCrawlRateInput!]! = []
                  minDescriptionLength: Int! = 50
                  minTitleLength: Int! = 10
                  minVisits: Int! = 2
                  mobileHomepageUrl: String = null
                  mobileUrlPattern: String = null
                  mobileUserAgentCode: String! = "googlebot-smartphone"
                  mobileViewportHeight: Int
                  mobileViewportWidth: Int
                  name: String!
                  primaryDomain: String!
                  renderTimeout: Int
                  renderWithImages: Boolean! = false
                  rendererBlockAds: Boolean! = true
                  rendererBlockAnalytics: Boolean! = true
                  rendererBlockCustom: [String!]! = []
                  rendererCookies: [RendererCookieInput!]! = []
                  rendererJsString: String = null
                  rendererJsUrls: [String!]! = []
                  renderingRobotsCheckMode: RenderingRobotsCheckMode! = BlockDisallowed
                  robotsOverwrite: String = null
                  secondaryDomains: [String!]! = []
                  selectedWcagLevel: WcagLevel! = AAA
                  selectedWcagVersion: Float! = 2.2
                  startUrls: [String!]! = []
                  targetMaxUncrawledUrlsCount: Int! = 500000
                  testSiteDomain: String = null
                  testSitePassword: String = null
                  testSiteUsername: String = null
                  thinPageThreshold: Int! = 3072
                  urlRewriteQueryParameters: [String!]! = []
                  urlRewriteRules: [UrlRewriteRuleInput!]! = []
                  urlRewriteStripFragment: Boolean! = true
                  urlSampling: [UrlSamplingInput!]! = []
                  useMobileSettings: Boolean! = false
                  useNewHeadlessMode: Boolean! = false
                  useRenderer: Boolean! = false
                  useRobotsOverwrite: Boolean! = false
                  useStealthMode: Boolean! = false
                  useUrlRewriteRules: Boolean! = false
                  userAgentCode: String! = "googlebot-smartphone"
                  userAgentIsMobile: Boolean = null
                  userAgentMobileIsMobile: Boolean = null
                  userAgentString: String = null
                  userAgentStringMobile: String = null
                  userAgentToken: String = null
                  userAgentTokenMobile: String = null
                  viewportHeight: Int
                  viewportWidth: Int
                }

        :param project_input: Project input
        :type project_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.createProject.args(input=project_input).select(
            self.ds.CreateProjectPayload.project.select(*fields or ProjectFields.fields(self.ds))
        )
        return self.conn.run_mutation(mutation)

    def update_project(self, project_input, fields=None):
        """Updates a Project

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input UpdateProjectInput {
                  alertEmails: [String!]
                  alertSettingCode: AlertSettingCode
                  apiCallbackHeaders: [APICallbackHeaderInput!]
                  apiCallbackUrl: String
                  applyCustomHeadersToNavigationRequestsOnly: Boolean
                  autoFinalizeOnCrawlLimits: Boolean
                  block3rdPartyCookies: Boolean
                  compareToCrawl: CompareToCrawl
                  crawlDisallowedUrls1stLevel: Boolean
                  crawlHyperlinksExternal: Boolean
                  crawlHyperlinksInternal: Boolean
                  crawlImagesExternal: Boolean
                  crawlImagesInternal: Boolean
                  crawlNofollowHyperlinks: Boolean
                  crawlNonHtml: Boolean
                  crawlNotIncluded1stLevel: Boolean
                  crawlRedirectsExternal: Boolean
                  crawlRedirectsInternal: Boolean
                  crawlRelAmphtmlExternal: Boolean
                  crawlRelAmphtmlInternal: Boolean
                  crawlRelCanonicalsExternal: Boolean
                  crawlRelCanonicalsInternal: Boolean
                  crawlRelHreflangsExternal: Boolean
                  crawlRelHreflangsInternal: Boolean
                  crawlRelMobileExternal: Boolean
                  crawlRelMobileInternal: Boolean
                  crawlRelNextPrevExternal: Boolean
                  crawlRelNextPrevInternal: Boolean
                  crawlRobotsTxtNoindex: Boolean
                  crawlScriptsExternal: Boolean
                  crawlScriptsInternal: Boolean
                  crawlStylesheetsExternal: Boolean
                  crawlStylesheetsInternal: Boolean
                  crawlTestSite: Boolean
                  crawlTypes: [CrawlType!]
                  customDns: [CustomDnsSettingInput!]
                  customExtractions: [CustomExtractionSettingInput!]
                  customRequestHeaders: [CustomRequestHeaderInput!]
                  dataLayerName: String
                  dataOnlyCrawlTypes: [CrawlType!]
                  discoverSitemapsInRobotsTxt: Boolean
                  duplicatePrecision: Float
                  emptyPageThreshold: Int
                  enableKeyValueStore: Boolean
                  excludeUrlPatterns: [String!]
                  excludedDatasources: [DatasourceCode!]
                  failureRateLimitEnabled: Boolean
                  failureRateLookbackWindow: Int
                  failureRateThreshold: Float
                  flattenIframes: Boolean
                  flattenShadowDom: Boolean
                  gaDateRange: Int
                  ignoreInvalidSSLCertificate: Boolean
                  ignoreRobotsForNavigationRequests: Boolean
                  includeBestPractices: Boolean
                  includeHttpAndHttps: Boolean
                  includeSubdomains: Boolean
                  includeUrlPatterns: [String!]
                  industryCode: String
                  limitLevelsMax: Int
                  limitUrlsMax: Int
                  locationCode: LocationCode
                  logSummaryRequestsHigh: Int
                  logSummaryRequestsLow: Int
                  maxBodyContentLength: Int
                  maxDescriptionLength: Int
                  maxFollowedExternalLinks: Int
                  maxHtmlSize: Int
                  maxLinks: Int
                  maxLoadTime: Float
                  maxRedirections: Int
                  maxTitleWidth: Int
                  maxUrlLength: Int
                  maximumCrawlRate: Float
                  maximumCrawlRateAdvanced: [AdvancedCrawlRateInput!]
                  minContentRatio: Float
                  minDescriptionLength: Int
                  minTitleLength: Int
                  minVisits: Int
                  mobileHomepageUrl: String
                  mobileUrlPattern: String
                  mobileUserAgentCode: String
                  mobileViewportHeight: Int
                  mobileViewportWidth: Int
                  name: String
                  primaryDomain: String
                  projectId: ObjectID!
                  renderTimeout: Int
                  renderWithImages: Boolean
                  rendererBlockAds: Boolean
                  rendererBlockAnalytics: Boolean
                  rendererBlockCustom: [String!]
                  rendererCookies: [RendererCookieInput!]
                  rendererJsString: String
                  rendererJsUrls: [String!]
                  renderingRobotsCheckMode: RenderingRobotsCheckMode
                  robotsOverwrite: String
                  secondaryDomains: [String!]
                  selectedWcagLevel: WcagLevel
                  selectedWcagVersion: Float
                  startUrls: [String!]
                  targetMaxUncrawledUrlsCount: Int
                  testSiteDomain: String
                  testSitePassword: String
                  testSiteUsername: String
                  thinPageThreshold: Int
                  urlRewriteQueryParameters: [String!]
                  urlRewriteRules: [UrlRewriteRuleInput!]
                  urlRewriteStripFragment: Boolean
                  urlSampling: [UrlSamplingInput!]
                  useMobileSettings: Boolean
                  useNewHeadlessMode: Boolean
                  useRenderer: Boolean
                  useRobotsOverwrite: Boolean
                  useStealthMode: Boolean
                  useUrlRewriteRules: Boolean
                  userAgentCode: String
                  userAgentIsMobile: Boolean
                  userAgentMobileIsMobile: Boolean
                  userAgentString: String
                  userAgentStringMobile: String
                  userAgentToken: String
                  userAgentTokenMobile: String
                  viewportHeight: Int
                  viewportWidth: Int
                }

        :param project_input: Project input
        :type project_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.updateProject.args(input=project_input).select(
            self.ds.UpdateProjectPayload.project.select(*fields or ProjectFields.fields(self.ds))
        )
        return self.conn.run_mutation(mutation)

    def create_accessibility_project(self, project_input, fields=None):
        """Creates an Accessibility Project

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input CreateAccessibilityProjectInput {
                  accountId: ObjectID!
                  alertEmails: [String!]
                  alertSettingCode: AlertSettingCode! = Always
                  apiCallbackHeaders: [APICallbackHeaderInput!]! = []
                  apiCallbackUrl: String = null
                  applyCustomHeadersToNavigationRequestsOnly: Boolean! = false
                  autoFinalizeOnCrawlLimits: Boolean! = true
                  block3rdPartyCookies: Boolean! = false
                  compareToCrawl: CompareToCrawlType! = LastCrawl
                  crawlDisallowedUrls1stLevel: Boolean! = false
                  crawlHyperlinksExternal: Boolean! = false
                  crawlHyperlinksInternal: Boolean! = true
                  crawlImagesExternal: Boolean! = false
                  crawlImagesInternal: Boolean! = false
                  crawlNofollowHyperlinks: Boolean! = true
                  crawlNonHtml: Boolean! = false
                  crawlNotIncluded1stLevel: Boolean! = false
                  crawlRedirectsExternal: Boolean! = true
                  crawlRedirectsInternal: Boolean! = true
                  crawlRelAmphtmlExternal: Boolean! = false
                  crawlRelAmphtmlInternal: Boolean! = true
                  crawlRelCanonicalsExternal: Boolean! = false
                  crawlRelCanonicalsInternal: Boolean! = true
                  crawlRelHreflangsExternal: Boolean! = false
                  crawlRelHreflangsInternal: Boolean! = true
                  crawlRelMobileExternal: Boolean! = false
                  crawlRelMobileInternal: Boolean! = true
                  crawlRelNextPrevExternal: Boolean! = false
                  crawlRelNextPrevInternal: Boolean! = true
                  crawlRobotsTxtNoindex: Boolean! = true
                  crawlScriptsExternal: Boolean! = false
                  crawlScriptsInternal: Boolean! = false
                  crawlStylesheetsExternal: Boolean! = false
                  crawlStylesheetsInternal: Boolean! = false
                  crawlTestSite: Boolean! = false
                  crawlTypes: [CrawlType!]! = [Web]
                  customDns: [CustomDnsSettingInput!]! = []
                  customExtractions: [CustomExtractionSettingInput!]! = []
                  customRequestHeaders: [CustomRequestHeaderInput!]! = []
                  dataLayerName: String = null
                  dataOnlyCrawlTypes: [CrawlType!]
                  discoverSitemapsInRobotsTxt: Boolean! = true
                  duplicatePrecision: Float! = 3
                  emptyPageThreshold: Int! = 512
                  enableKeyValueStore: Boolean! = false
                  excludeUrlPatterns: [String!]! = []
                  excludedDatasources: [DatasourceCode!]
                  failureRateLimitEnabled: Boolean! = false
                  failureRateLookbackWindow: Int! = 300
                  failureRateThreshold: Float! = 50
                  flattenIframes: Boolean! = false
                  flattenShadowDom: Boolean! = false
                  gaDateRange: Int! = 30
                  ignoreInvalidSSLCertificate: Boolean! = false
                  ignoreRobotsForNavigationRequests: Boolean! = true
                  includeBestPractices: Boolean! = true
                  includeHttpAndHttps: Boolean! = false
                  includeSubdomains: Boolean! = false
                  includeUrlPatterns: [String!]! = []
                  industryCode: String
                  limitLevelsMax: Int
                  limitUrlsMax: Int
                  locationCode: LocationCode! = Default
                  logSummaryRequestsHigh: Int! = 100
                  logSummaryRequestsLow: Int! = 10
                  maxBodyContentLength: Int! = 51200
                  maxDescriptionLength: Int! = 230
                  maxFollowedExternalLinks: Int! = 10
                  maxHtmlSize: Int! = 204800
                  maxLinks: Int! = 250
                  maxLoadTime: Float! = 3
                  maxRedirections: Int! = 4
                  maxTitleWidth: Int! = 600
                  maxUrlLength: Int! = 1024
                  maximumCrawlRate: Float! = 3
                  maximumCrawlRateAdvanced: [AdvancedCrawlRateInput!]! = []
                  minDescriptionLength: Int! = 50
                  minTitleLength: Int! = 10
                  minVisits: Int! = 2
                  mobileHomepageUrl: String = null
                  mobileUrlPattern: String = null
                  mobileUserAgentCode: String! = "chrome-a11y-mobile"
                  mobileViewportHeight: Int
                  mobileViewportWidth: Int
                  name: String!
                  primaryDomain: String!
                  renderTimeout: Int
                  renderWithImages: Boolean! = false
                  rendererBlockAds: Boolean! = false
                  rendererBlockAnalytics: Boolean! = true
                  rendererBlockCustom: [String!]! = []
                  rendererCookies: [RendererCookieInput!]! = []
                  rendererJsString: String = null
                  rendererJsUrls: [String!]! = []
                  renderingRobotsCheckMode: RenderingRobotsCheckMode! = RequestDisallowed
                  robotsOverwrite: String = null
                  secondaryDomains: [String!]! = []
                  selectedWcagLevel: WcagLevel! = AAA
                  selectedWcagVersion: Float! = 2.2
                  startUrls: [String!]! = []
                  storeHtml: Boolean! = false
                  targetMaxUncrawledUrlsCount: Int! = 500000
                  testSiteDomain: String = null
                  testSitePassword: String = null
                  testSiteUsername: String = null
                  thinPageThreshold: Int! = 3072
                  urlRewriteQueryParameters: [String!]! = []
                  urlRewriteRules: [UrlRewriteRuleInput!]! = []
                  urlRewriteStripFragment: Boolean! = true
                  urlSampling: [UrlSamplingInput!]! = []
                  useMobileSettings: Boolean! = false
                  useNewHeadlessMode: Boolean! = false
                  useRobotsOverwrite: Boolean! = false
                  useStealthMode: Boolean! = false
                  useStealthModeV2: Boolean! = false
                  useUrlRewriteRules: Boolean! = false
                  userAgentCode: String! = "googlebot-smartphone"
                  userAgentIsMobile: Boolean = null
                  userAgentMobileIsMobile: Boolean = null
                  userAgentString: String = null
                  userAgentStringMobile: String = null
                  userAgentToken: String = null
                  userAgentTokenMobile: String = null
                  viewportHeight: Int
                  viewportWidth: Int
                }

        :param project_input: Project input
        :type project_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.createAccessibilityProject.args(input=project_input).select(
            self.ds.CreateProjectPayload.project.select(*fields or ProjectFields.fields(self.ds))
        )
        return self.conn.run_mutation(mutation)

    def delete_project(self, project_id, fields=None):
        """Deletes a Project

        :param project_id: Project id
        :type project_id: int or str
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.deleteProject.args(projectId=project_id).select(
            self.ds.DeleteProjectPayload.project.select(*fields or ProjectFields.fields(self.ds))
        )
        return self.conn.run_mutation(mutation)

    def update_majestic_configuration(self, majestic_configuration_input, fields=None):
        """Updates a MajesticConfiguration

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input UpdateMajesticConfigurationInput {
                  enabled: Boolean
                  maxRows: Int
                  projectId: ObjectID!
                  useHistoricData: Boolean
                  useRootDomain: Boolean
                }

        :param majestic_configuration_input: MajesticConfigurationInput
        :type majestic_configuration_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.updateMajesticConfiguration.args(input=majestic_configuration_input).select(
            self.ds.UpdateMajesticConfigurationPayload.majesticConfiguration.select(
                *fields or ProjectFields.majestic_configuration_fields(self.ds)
            )
        )
        return self.conn.run_mutation(mutation)

    """
    Schedules
    """

    def create_schedule(self, schedule_input, fields=None):
        """Creates a Schedule

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input CreateScheduleInput {
                  nextRunTime: DateTime!
                  projectId: ObjectID!
                  scheduleFrequency: ScheduleFrequencyCode!
                }

        :param schedule_input: CreateScheduleInput
        :type schedule_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.createSchedule.args(input=schedule_input).select(
            self.ds.CreateSchedulePayload.schedule.select(
                *fields or ProjectFields.schedule_fields(self.ds)
            )
        )
        return self.conn.run_mutation(mutation)

    def update_schedule(self, schedule_input, fields=None):
        """Updates a Schedule

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input UpdateScheduleInput {
                  scheduleId: ObjectID!
                  nextRunTime: DateTime
                  scheduleFrequency: ScheduleFrequencyCode
                }

        :param schedule_input: UpdateScheduleInput
        :type schedule_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.updateSchedule.args(input=schedule_input).select(
            self.ds.UpdateSchedulePayload.schedule.select(
                *fields or ProjectFields.schedule_fields(self.ds)
            )
        )
        return self.conn.run_mutation(mutation)

    def delete_schedule(self, schedule_input, fields=None):
        """Deletes a Schedule

        .. dropdown:: GraphQL Input Example

            It has to be converted to dict

            .. code-block::

                input DeleteScheduleInput {
                  scheduleId: ObjectID!
                }

        :param schedule_input: DeleteScheduleInput
        :type schedule_input: dict
        :param fields: Select specific fields
        :type fields: List(DSLField)
        """
        mutation = self.mutation.deleteSchedule.args(input=schedule_input).select(
            self.ds.DeleteSchedulePayload.schedule.select(
                *fields or ProjectFields.schedule_fields(self.ds)
            )
        )
        return self.conn.run_mutation(mutation)
