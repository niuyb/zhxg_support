# Generated by Django 2.2.4 on 2020-02-11 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secretary', '0002_dinggroupmembermap'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AgentsInfo',
        ),
        migrations.DeleteModel(
            name='AppImportData',
        ),
        migrations.DeleteModel(
            name='AppUsageStatistics',
        ),
        migrations.DeleteModel(
            name='Artificialearlywarning',
        ),
        migrations.DeleteModel(
            name='BakWkTUser20190915',
        ),
        migrations.DeleteModel(
            name='CalIdf',
        ),
        migrations.DeleteModel(
            name='CalIdfdocnum',
        ),
        migrations.DeleteModel(
            name='Checkurlcollection',
        ),
        migrations.DeleteModel(
            name='Checkurljob',
        ),
        migrations.DeleteModel(
            name='Cityhot',
        ),
        migrations.DeleteModel(
            name='Classlyproject',
        ),
        migrations.DeleteModel(
            name='Classlyrule',
        ),
        migrations.DeleteModel(
            name='Classlyrule1',
        ),
        migrations.DeleteModel(
            name='Classlyruleclassly',
        ),
        migrations.DeleteModel(
            name='Config',
        ),
        migrations.DeleteModel(
            name='CrmaccountmappingBak20191209',
        ),
        migrations.DeleteModel(
            name='Crmaccountsalemapping',
        ),
        migrations.DeleteModel(
            name='Crmsalemapping',
        ),
        migrations.DeleteModel(
            name='Crmtimelinedata',
        ),
        migrations.DeleteModel(
            name='Crmwpmapping',
        ),
        migrations.DeleteModel(
            name='DatacountAccurateCondition',
        ),
        migrations.DeleteModel(
            name='Domaincount',
        ),
        migrations.DeleteModel(
            name='Domainweight',
        ),
        migrations.DeleteModel(
            name='HomepageHeadlinesInfo',
        ),
        migrations.DeleteModel(
            name='Indexpart',
        ),
        migrations.DeleteModel(
            name='Indexpartmapping',
        ),
        migrations.DeleteModel(
            name='IndexSalerData',
        ),
        migrations.DeleteModel(
            name='IndexSalerProfileData',
        ),
        migrations.DeleteModel(
            name='Infoclassly',
        ),
        migrations.DeleteModel(
            name='IpAddress',
        ),
        migrations.DeleteModel(
            name='LawProtect',
        ),
        migrations.DeleteModel(
            name='Mobilecloudcourse',
        ),
        migrations.DeleteModel(
            name='Mobilecloudcourselectuer',
        ),
        migrations.DeleteModel(
            name='Mobilecloudcourseware',
        ),
        migrations.DeleteModel(
            name='Mobilecloudevent',
        ),
        migrations.DeleteModel(
            name='Mobilecloudsubject',
        ),
        migrations.DeleteModel(
            name='MobileLibrary',
        ),
        migrations.DeleteModel(
            name='MsAccount',
        ),
        migrations.DeleteModel(
            name='MsApiStatusLog',
        ),
        migrations.DeleteModel(
            name='MsEventKeywordsGroup',
        ),
        migrations.DeleteModel(
            name='MsEventKeywordsGroupSubjectRelation',
        ),
        migrations.DeleteModel(
            name='MsOutbox',
        ),
        migrations.DeleteModel(
            name='MsShareInfo',
        ),
        migrations.DeleteModel(
            name='MsSourceType',
        ),
        migrations.DeleteModel(
            name='MysqlDatasourceConfig',
        ),
        migrations.DeleteModel(
            name='Newwords',
        ),
        migrations.DeleteModel(
            name='Newwordsclassly',
        ),
        migrations.DeleteModel(
            name='Notwords',
        ),
        migrations.DeleteModel(
            name='OfficalAdvertise',
        ),
        migrations.DeleteModel(
            name='OfficalNews',
        ),
        migrations.DeleteModel(
            name='OfficalNewsContent',
        ),
        migrations.DeleteModel(
            name='OverseaSwitchChangeLog',
        ),
        migrations.DeleteModel(
            name='OverseaWeb',
        ),
        migrations.DeleteModel(
            name='OverseaWebtype',
        ),
        migrations.DeleteModel(
            name='Pnwords',
        ),
        migrations.DeleteModel(
            name='PreservationEvidenceApply',
        ),
        migrations.DeleteModel(
            name='PreservationEvidenceApplyRecord',
        ),
        migrations.DeleteModel(
            name='PreservationEvidenceRecord',
        ),
        migrations.DeleteModel(
            name='Projectclassly',
        ),
        migrations.DeleteModel(
            name='PushRegistInfoBak',
        ),
        migrations.DeleteModel(
            name='Reportclassify',
        ),
        migrations.DeleteModel(
            name='Reportfileinfo',
        ),
        migrations.DeleteModel(
            name='ReportTemplate',
        ),
        migrations.DeleteModel(
            name='Reportvariable',
        ),
        migrations.DeleteModel(
            name='Reportwords',
        ),
        migrations.DeleteModel(
            name='Saledatacount',
        ),
        migrations.DeleteModel(
            name='Salespart',
        ),
        migrations.DeleteModel(
            name='Salespartmapping',
        ),
        migrations.DeleteModel(
            name='SolrTCollectinfo',
        ),
        migrations.DeleteModel(
            name='SolrTCollectinfocnt',
        ),
        migrations.DeleteModel(
            name='SolrTExportcondition',
        ),
        migrations.DeleteModel(
            name='SolrTExportfield',
        ),
        migrations.DeleteModel(
            name='SubCompletionLog',
        ),
        migrations.DeleteModel(
            name='Subjectrelationlable',
        ),
        migrations.DeleteModel(
            name='SubjectUnselect',
        ),
        migrations.DeleteModel(
            name='SyncMonitor',
        ),
        migrations.DeleteModel(
            name='SystemTask',
        ),
        migrations.DeleteModel(
            name='TaskCenter',
        ),
        migrations.DeleteModel(
            name='TaskRequestInfo',
        ),
        migrations.DeleteModel(
            name='TC3P0Test',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Test199',
        ),
        migrations.DeleteModel(
            name='Test199Yj',
        ),
        migrations.DeleteModel(
            name='Testdataapi',
        ),
        migrations.DeleteModel(
            name='Testweiwen',
        ),
        migrations.DeleteModel(
            name='Topicauthorrelation',
        ),
        migrations.DeleteModel(
            name='Topicgdlines',
        ),
        migrations.DeleteModel(
            name='Topicrdpoint',
        ),
        migrations.DeleteModel(
            name='Topictfpoint',
        ),
        migrations.DeleteModel(
            name='Topicweiboauthorinfo',
        ),
        migrations.DeleteModel(
            name='Trainclassly',
        ),
        migrations.DeleteModel(
            name='Travelplantemplate',
        ),
        migrations.DeleteModel(
            name='Userdatacount',
        ),
        migrations.DeleteModel(
            name='Userdatestatuscount',
        ),
        migrations.DeleteModel(
            name='UserFilterKeyword',
        ),
        migrations.DeleteModel(
            name='Userpushnum',
        ),
        migrations.DeleteModel(
            name='UsersetChangeIllustrate',
        ),
        migrations.DeleteModel(
            name='Usertimelong',
        ),
        migrations.DeleteModel(
            name='WarningServiceApplication',
        ),
        migrations.DeleteModel(
            name='WarningServiceApplicationLog',
        ),
        migrations.DeleteModel(
            name='Warningstatuslog',
        ),
        migrations.DeleteModel(
            name='Warningtimesetting',
        ),
        migrations.DeleteModel(
            name='Warningtimesettingsystem',
        ),
        migrations.DeleteModel(
            name='Weibocomminfo',
        ),
        migrations.DeleteModel(
            name='WeixinCorpid',
        ),
        migrations.DeleteModel(
            name='WeixinPush',
        ),
        migrations.DeleteModel(
            name='WkTAccessNew',
        ),
        migrations.DeleteModel(
            name='WkTAgency',
        ),
        migrations.DeleteModel(
            name='WkTAgencyLoginPage',
        ),
        migrations.DeleteModel(
            name='WkTAgentApp',
        ),
        migrations.DeleteModel(
            name='WkTAgentAppJoblog',
        ),
        migrations.DeleteModel(
            name='WkTAgentAppStatus',
        ),
        migrations.DeleteModel(
            name='WkTAgentGroup',
        ),
        migrations.DeleteModel(
            name='WkTAgentNew',
        ),
        migrations.DeleteModel(
            name='WkTAgents',
        ),
        migrations.DeleteModel(
            name='WkTAgentuserGroup',
        ),
        migrations.DeleteModel(
            name='WkTAllexport',
        ),
        migrations.DeleteModel(
            name='WkTAnnualReport',
        ),
        migrations.DeleteModel(
            name='WkTAppedition',
        ),
        migrations.DeleteModel(
            name='WkTAppeditionZj',
        ),
        migrations.DeleteModel(
            name='WkTApply',
        ),
        migrations.DeleteModel(
            name='WkTAppSite',
        ),
        migrations.DeleteModel(
            name='WkTApptvedition',
        ),
        migrations.DeleteModel(
            name='WkTArea',
        ),
        migrations.DeleteModel(
            name='WkTAreaKeyws',
        ),
        migrations.DeleteModel(
            name='WkTBackendBlock',
        ),
        migrations.DeleteModel(
            name='WkTBackendframe',
        ),
        migrations.DeleteModel(
            name='WkTBackendRef',
        ),
        migrations.DeleteModel(
            name='WkTBackendRm',
        ),
        migrations.DeleteModel(
            name='WkTBackendrole',
        ),
        migrations.DeleteModel(
            name='WkTBar',
        ),
        migrations.DeleteModel(
            name='WkTBarnew',
        ),
        migrations.DeleteModel(
            name='WkTBarnewBack',
        ),
        migrations.DeleteModel(
            name='WkTBasekeytype',
        ),
        migrations.DeleteModel(
            name='WkTBasekeyws',
        ),
        migrations.DeleteModel(
            name='WkTBelongkefuNew',
        ),
        migrations.DeleteModel(
            name='WkTChannelTv',
        ),
        migrations.DeleteModel(
            name='WkTChannelUser',
        ),
        migrations.DeleteModel(
            name='WkTClassification',
        ),
        migrations.DeleteModel(
            name='WkTCommonKeyws',
        ),
        migrations.DeleteModel(
            name='WkTCompanyChangeinfo',
        ),
        migrations.DeleteModel(
            name='WkTCompanyUser',
        ),
        migrations.DeleteModel(
            name='WkTCourtannouncement',
        ),
        migrations.DeleteModel(
            name='WkTCustomCondition',
        ),
        migrations.DeleteModel(
            name='WkTCustomConditionField',
        ),
        migrations.DeleteModel(
            name='WkTCustomConditionSub',
        ),
        migrations.DeleteModel(
            name='WkTCustomConditionValue',
        ),
        migrations.DeleteModel(
            name='WkTDatasourcetype',
        ),
        migrations.DeleteModel(
            name='WkTDefinedhomeExtend',
        ),
        migrations.DeleteModel(
            name='WkTDelete',
        ),
        migrations.DeleteModel(
            name='WkTDeleteinfoLog',
        ),
        migrations.DeleteModel(
            name='WkTDeleteinfoLog1',
        ),
        migrations.DeleteModel(
            name='WkTDeleteinfoLog2',
        ),
        migrations.DeleteModel(
            name='WkTDeleteinfoSource',
        ),
        migrations.DeleteModel(
            name='WkTDeleterefReason',
        ),
        migrations.DeleteModel(
            name='WkTDept',
        ),
        migrations.DeleteModel(
            name='WkTDingdinggroup',
        ),
        migrations.DeleteModel(
            name='WkTDinguser',
        ),
        migrations.DeleteModel(
            name='WkTDinguserJob',
        ),
        migrations.DeleteModel(
            name='WkTDinguserNew',
        ),
        migrations.DeleteModel(
            name='WkTDishonest',
        ),
        migrations.DeleteModel(
            name='WkTEnforcement',
        ),
        migrations.DeleteModel(
            name='WkTEverydaydata',
        ),
        migrations.DeleteModel(
            name='WkTFullsearchCatalog',
        ),
        migrations.DeleteModel(
            name='WkTHelp',
        ),
        migrations.DeleteModel(
            name='WkTHelpClass',
        ),
        migrations.DeleteModel(
            name='WkTHljCourtUser',
        ),
        migrations.DeleteModel(
            name='WkTHomekeysset',
        ),
        migrations.DeleteModel(
            name='WkTHomepage',
        ),
        migrations.DeleteModel(
            name='WkTHomesite',
        ),
        migrations.DeleteModel(
            name='WkTHotinfo',
        ),
        migrations.DeleteModel(
            name='WkTHotinfo3',
        ),
        migrations.DeleteModel(
            name='WkTId',
        ),
        migrations.DeleteModel(
            name='WkTIdCopy',
        ),
        migrations.DeleteModel(
            name='WkTIndexModule',
        ),
        migrations.DeleteModel(
            name='WkTIndKeyws',
        ),
        migrations.DeleteModel(
            name='WkTIndustry',
        ),
        migrations.DeleteModel(
            name='WkTInfo',
        ),
        migrations.DeleteModel(
            name='WkTInfoSource',
        ),
        migrations.DeleteModel(
            name='WkTIpinfo',
        ),
        migrations.DeleteModel(
            name='WkTJobOffers',
        ),
        migrations.DeleteModel(
            name='WkTJudgment',
        ),
        migrations.DeleteModel(
            name='WkTJudicialsale',
        ),
        migrations.DeleteModel(
            name='WkTKefupowerNew',
        ),
        migrations.DeleteModel(
            name='WkTKeyws',
        ),
        migrations.DeleteModel(
            name='WkTKeyws1',
        ),
        migrations.DeleteModel(
            name='WkTKeyws2',
        ),
        migrations.DeleteModel(
            name='WkTKeywsBackend',
        ),
        migrations.DeleteModel(
            name='WkTKeywsCopy',
        ),
        migrations.DeleteModel(
            name='WkTKeywsCopy1',
        ),
        migrations.DeleteModel(
            name='WkTKeywsCopy2',
        ),
        migrations.DeleteModel(
            name='WkTKeywsLog',
        ),
        migrations.DeleteModel(
            name='WkTKeywsWarnset',
        ),
        migrations.DeleteModel(
            name='WkTLocationuserBasicnumber',
        ),
        migrations.DeleteModel(
            name='WkTLocationuserCoverage',
        ),
        migrations.DeleteModel(
            name='WkTManagerLog',
        ),
        migrations.DeleteModel(
            name='WkTMessage',
        ),
        migrations.DeleteModel(
            name='WkTModuleinfo',
        ),
        migrations.DeleteModel(
            name='WkTMuser',
        ),
        migrations.DeleteModel(
            name='WkTMuserCount',
        ),
        migrations.DeleteModel(
            name='WkTMycollection',
        ),
        migrations.DeleteModel(
            name='WkTNewbackendLog',
        ),
        migrations.DeleteModel(
            name='WkTNodeNew',
        ),
        migrations.DeleteModel(
            name='WkTPatent',
        ),
        migrations.DeleteModel(
            name='WkTPhoneInfo',
        ),
        migrations.DeleteModel(
            name='WkTPhonelist',
        ),
        migrations.DeleteModel(
            name='WkTPhonepush',
        ),
        migrations.DeleteModel(
            name='WkTProductLog',
        ),
        migrations.DeleteModel(
            name='WkTQqkeyws',
        ),
        migrations.DeleteModel(
            name='WkTRegisteruser',
        ),
        migrations.DeleteModel(
            name='WkTReport',
        ),
        migrations.DeleteModel(
            name='WkTReportPush',
        ),
        migrations.DeleteModel(
            name='WkTReporttemplate',
        ),
        migrations.DeleteModel(
            name='WkTRole2',
        ),
        migrations.DeleteModel(
            name='WkTRoleNew',
        ),
        migrations.DeleteModel(
            name='WkTRoletitle',
        ),
        migrations.DeleteModel(
            name='WkTRoleuserNew',
        ),
        migrations.DeleteModel(
            name='WkTSearchCondition',
        ),
        migrations.DeleteModel(
            name='WkTSearchConditionCopy',
        ),
        migrations.DeleteModel(
            name='WkTSearchword',
        ),
        migrations.DeleteModel(
            name='WkTShare',
        ),
        migrations.DeleteModel(
            name='WkTSoftwareCopyright',
        ),
        migrations.DeleteModel(
            name='WkTSubjectWordLength',
        ),
        migrations.DeleteModel(
            name='WkTTitle2',
        ),
        migrations.DeleteModel(
            name='WkTTopickeywordcheck',
        ),
        migrations.DeleteModel(
            name='WkTTrademark',
        ),
        migrations.DeleteModel(
            name='WkTUloguser',
        ),
        migrations.DeleteModel(
            name='WkTUpdatelog',
        ),
        migrations.DeleteModel(
            name='WkTUpdaterecord',
        ),
        migrations.DeleteModel(
            name='WkTUpdaterecordZj',
        ),
        migrations.DeleteModel(
            name='WkTUpdatetvrecord',
        ),
        migrations.DeleteModel(
            name='WkTUploadFile',
        ),
        migrations.DeleteModel(
            name='WkTUploadFolder',
        ),
        migrations.DeleteModel(
            name='WkTUsearchword',
        ),
        migrations.DeleteModel(
            name='WkTUserapi',
        ),
        migrations.DeleteModel(
            name='WkTUserApplicationLog',
        ),
        migrations.DeleteModel(
            name='WkTUserArea',
        ),
        migrations.DeleteModel(
            name='WkTUserAreaNew',
        ),
        migrations.DeleteModel(
            name='WkTUserAreaNew1',
        ),
        migrations.DeleteModel(
            name='WkTUserbaseinfo',
        ),
        migrations.DeleteModel(
            name='WkTUserbaseinfoCopy',
        ),
        migrations.DeleteModel(
            name='WkTUsercheck',
        ),
        migrations.DeleteModel(
            name='WkTUserclassify',
        ),
        migrations.DeleteModel(
            name='WkTUserclassifySystem',
        ),
        migrations.DeleteModel(
            name='WkTUsercustom',
        ),
        migrations.DeleteModel(
            name='WkTUserDailycount',
        ),
        migrations.DeleteModel(
            name='WkTUserDept',
        ),
        migrations.DeleteModel(
            name='WkTUserfeedback',
        ),
        migrations.DeleteModel(
            name='WkTUserfieldattribute',
        ),
        migrations.DeleteModel(
            name='WkTUserInd',
        ),
        migrations.DeleteModel(
            name='WkTUserindexModule',
        ),
        migrations.DeleteModel(
            name='WkTUserLocalyjkeyws',
        ),
        migrations.DeleteModel(
            name='WkTUserLoginLog',
        ),
        migrations.DeleteModel(
            name='WkTUsermail',
        ),
        migrations.DeleteModel(
            name='WkTUsermailExport',
        ),
        migrations.DeleteModel(
            name='WkTUsermodule',
        ),
        migrations.DeleteModel(
            name='WkTUsermoduledetails',
        ),
        migrations.DeleteModel(
            name='WkTUsermodulefieldtype',
        ),
        migrations.DeleteModel(
            name='WkTUsermodulerelation',
        ),
        migrations.DeleteModel(
            name='WkTUsernav',
        ),
        migrations.DeleteModel(
            name='WkTUserole2',
        ),
        migrations.DeleteModel(
            name='WkTUserpsw',
        ),
        migrations.DeleteModel(
            name='WkTUserRemarks',
        ),
        migrations.DeleteModel(
            name='WkTUserserviceBak',
        ),
        migrations.DeleteModel(
            name='WkTUsersource',
        ),
        migrations.DeleteModel(
            name='WkTUserStatusLog',
        ),
        migrations.DeleteModel(
            name='WkTUsertemplate',
        ),
        migrations.DeleteModel(
            name='WkTUserweb',
        ),
        migrations.DeleteModel(
            name='WkTUserYjkeyws',
        ),
        migrations.DeleteModel(
            name='WkTValidationInfo',
        ),
        migrations.DeleteModel(
            name='WkTValidationInfocnt',
        ),
        migrations.DeleteModel(
            name='WkTValidationYjinfo',
        ),
        migrations.DeleteModel(
            name='WkTValidationYjinfocnt',
        ),
        migrations.DeleteModel(
            name='WkTVersionupgradeLog',
        ),
        migrations.DeleteModel(
            name='WkTVideo',
        ),
        migrations.DeleteModel(
            name='WkTVideorecord',
        ),
        migrations.DeleteModel(
            name='WkTWarnaccDinguser',
        ),
        migrations.DeleteModel(
            name='WkTWarnaccUser',
        ),
        migrations.DeleteModel(
            name='WkTWarnspecialAlldinguser',
        ),
        migrations.DeleteModel(
            name='WkTWarnspecialDinguser',
        ),
        migrations.DeleteModel(
            name='WkTWarnspecialUser',
        ),
        migrations.DeleteModel(
            name='WkTWebsite',
        ),
        migrations.DeleteModel(
            name='WkTWebuserbacklog',
        ),
        migrations.DeleteModel(
            name='WkTWebuserlog',
        ),
        migrations.DeleteModel(
            name='WkTWorkcopyright',
        ),
        migrations.DeleteModel(
            name='WkTWtfk',
        ),
        migrations.DeleteModel(
            name='WkTWtfkCnt',
        ),
        migrations.DeleteModel(
            name='WkTWxkeyws',
        ),
        migrations.DeleteModel(
            name='WkTYqjb1',
        ),
        migrations.DeleteModel(
            name='WkTYqmsonlyuser',
        ),
        migrations.DeleteModel(
            name='WkTYqmsywpushnews',
        ),
        migrations.DeleteModel(
            name='WkTYqmsywuser',
        ),
        migrations.DeleteModel(
            name='WkTYsDomain',
        ),
        migrations.DeleteModel(
            name='WkTYtjUser',
        ),
        migrations.DeleteModel(
            name='WkTYtjUserAreaNew',
        ),
        migrations.DeleteModel(
            name='WkTYtjUserbaseinfo',
        ),
        migrations.DeleteModel(
            name='WkTYtjUserservice',
        ),
        migrations.DeleteModel(
            name='WtKSubrelation',
        ),
        migrations.DeleteModel(
            name='WtKSubrelation2',
        ),
        migrations.DeleteModel(
            name='WtKSubrelationBackend',
        ),
        migrations.DeleteModel(
            name='WtKSubrelationBak20191016',
        ),
        migrations.DeleteModel(
            name='Yjclusteruser',
        ),
        migrations.DeleteModel(
            name='YqzbTCkey',
        ),
        migrations.DeleteModel(
            name='YqzbTEngineInfo',
        ),
        migrations.DeleteModel(
            name='YqzbTQq',
        ),
        migrations.DeleteModel(
            name='YqzbTQqmes',
        ),
        migrations.DeleteModel(
            name='YqzbTSyncLog',
        ),
        migrations.DeleteModel(
            name='YqzbTTopic',
        ),
        migrations.DeleteModel(
            name='YqzbTTopicModuleSummary',
        ),
        migrations.DeleteModel(
            name='YqzbTWeixin',
        ),
        migrations.DeleteModel(
            name='YqzbTWxmsg',
        ),
        migrations.DeleteModel(
            name='YqzbTYjxx',
        ),
        migrations.DeleteModel(
            name='ZhsqCompany',
        ),
        migrations.DeleteModel(
            name='ZhsqCompanyBaseinfo',
        ),
        migrations.DeleteModel(
            name='Zycluster',
        ),
        migrations.DeleteModel(
            name='Zyclusteruser',
        ),
        migrations.DeleteModel(
            name='Zywhiteuser',
        ),
        migrations.DeleteModel(
            name='Zywords',
        ),
    ]
