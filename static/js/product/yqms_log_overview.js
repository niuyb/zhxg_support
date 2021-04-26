function initYqmsLogOverviewVue() {
    new Vue({
        el: '#yqms_log_overview',
        delimiters: ["[[", "]]"],
        data() {
            return {
                filters: {},
                searchers: {},
                loading: true,
                needRetry: false,
                total: 0,
                pageIndex: 1,
                pageSize: 10,
                sourceTableData: [],
                tableData: [],
                footer: [],
                conditions: {},
                tableConfig: {
                    columnDict: {
                        "operate_date": "操作日期",
                        "operate_sum": "操作总数",
                        "pc40": "4.0PC操作",
                        "app40": "4.0APP操作",
                        "pc30": "3.0PC操作",
                        "app30": "3.0APP操作",
                        "wechat": "微信操作",
                    },
                    multipleSort: false,
                    tableData: [],
                    columns: [{
                        field: 'custome',
                        width: 60,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter: function (rowData, index, pagingIndex) {
                            var currentIndex = index + pagingIndex;
                            return currentIndex + 1
                        },
                        isFrozen: true
                    }, {
                        field: 'operate_date',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['operate_date'];
                            if (!value) {
                                return "----";
                            } else {
                                return value;
                            }
                        }
                    }, {
                        field: 'operate_sum',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['operate_sum'];
                            var uid = getUrlKey('uid', window.location.href);   // 获取当前页面的url中的uid的值
                            var account_name = getUrlKey('account_name', window.location.href);   // 获取当前页面的url中的account_name的值
                            var log_date = rowData['operate_date'];
                            log_date = log_date.replace("-", "");
                            log_date = log_date.replace("-", "");
                            if (value > 0) {
                                return "<a target='_blank' href='/product/yqms_accounts/yqms_log_detail?uid=" + uid + "&account_name=" + account_name + "&log_date=" + log_date + "'>" + value + "</a>";
                            } else {
                                return value;
                            }
                        }
                    }, {
                        field: 'pc40',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['pc40'];
                            return value;
                        }
                    }, {
                        field: 'app40',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['app40'];
                            return value;
                        }
                    }, {
                        field: 'pc30',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['pc30'];
                            return value;
                        }
                    }, {
                        field: 'app30',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['app30'];
                            return value;
                        }
                    }, {
                        field: 'wechat',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function (rowData, index, pagingIndex) {
                            var value = rowData['wechat'];
                            return value;
                        }
                    }],
                    titleRows: [[{
                        fields: ['custome'],
                        title: '序号',
                        titleAlign: 'center',
                        // orderBy: '',
                    }, {
                        fields: ['operate_date'],
                        title: '操作日期',
                        titleAlign: 'center',
                        orderBy: '',
                        // filterMultiple: false,
                        // filters: [{value: ""}],
                        isSearchAble: false,
                        // searchType: 'dateRange'
                    }, {
                        fields: ['operate_sum'],
                        title: '操作总数',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    }, {
                        fields: ['pc40'],
                        title: '4.0PC操作',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    }, {
                        fields: ['app40'],
                        title: '4.0APP操作',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    }, {
                        fields: ['pc30'],
                        title: '3.0PC操作',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    }, {
                        fields: ['app30'],
                        title: '3.0APP操作',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    }, {
                        fields: ['wechat'],
                        title: '微信操作',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    }]],
                },
                startDate: '',
                endDate: ''
            }
        },
        methods: {
            export_excel() {
                const req = new XMLHttpRequest();
                req.open('POST', '/product/yqms_accounts/export_log', true);
                req.responseType = 'blob';
                req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded'); //设置请求头
                req.send('start_time=' + $('#start_time').val() + '&end_time=' + $('#end_time').val() + '&uid=' + getUrlKey('uid', window.location.href)); //输入参数
                $('#export_excel').attr('disabled','true');
                $('#export_excel').text('导出中');
                req.onload = function() {
                const data = req.response;
                const blob = new Blob([data]);
                const blobUrl = window.URL.createObjectURL(blob);
                $('body').append("<a id = 'download' style='display: none' ></a>");
                $('#download').attr('href',blobUrl).attr('download',( new Date()).valueOf()+'.xls');
                $('#download')[0].click();
                $('#download')[0].remove();
                $('#export_excel').removeAttr('disabled');
                $('#export_excel').text('导出');
            }},
            getCommonFilters(field) {
                var filters = [];
                var js = {};
                for (var row of this.sourceTableData) {
                    var value = row[field];
                    var label = value;
                    if (value === "") {
                        label = "空";
                    }
                    if (!(js[value])) {
                        js[value] = true;
                        var item = {
                            label: label,
                            value: value
                        };
                        filters.push(item);
                    }
                }
                return filters;
            },
            // 根据各筛选条件、和排序条件，获取当前页面的数据，进行展示
            getTableShowData() {
                this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
            },
            // 从服务器获取原始数据
            //获取时间
            getTime(time) {
                var date = new Date();
                if (time == 'start_time') {
                    var n = new Date(date.getTime() - 86400000 * 7);
                } else {
                    var n = new Date(date.getTime() - 86400000);
                }
                var before_year = n.getFullYear();
                var before_month = n.getMonth() + 1 <= 9 ? "0" + (n.getMonth() + 1) : n.getMonth() + 1;
                var date2 = n.getDate() <= 9 ? "0" + n.getDate() : n.getDate();
                return before_year + '-' + before_month + '-' + date2;
            },
            getSourceTableData() {
                var self = this;
                var uid = getUrlKey('uid', window.location.href);   // 获取当前页面的url中的uid的
                var start_date = $('#start_time').val();
                if (start_date == null || start_date == '' || start_date == undefined || start_date == 'undefined') {
                    //     // date.setDate(date.getDate() - 7);
                    //     // start_date = date.toLocaleDateString().split('/').join('');
                    //     // // console.log(start_date.slice(0,8));
                    //     // if (start_date.length == 7) {
                    //     //     start_date = start_date.slice(0, 6) + '0' + start_date.slice(6);
                    //     // }
                    start_date = this.getTime('start_time');
                    //
                }
                var end_date = $('#end_time').val();
                if (end_date == null || end_date == '' || end_date == undefined || end_date == 'undefined') {
                    //     // var date = new Date();
                    //     // date.setDate(date.getDate() - 1);
                    //     // end_date = date.toLocaleDateString().split('/').join('');
                    //     // if (end_date.length == 7) {
                    //     //     end_date = end_date.slice(0, 6) + '0' + end_date.slice(6);
                    //     // }
                    end_date = this.getTime('end_time')
                }
                var url = '/product/yqms_accounts/yqms_log_overview_api?uid=' + uid + '&start_date=' + start_date + '&end_date=' + end_date;
                // console.log(url)
                axios.get(url, {
                    params: {
                        'page': 1,
                        "num": 0
                    }
                }).then(function (res) {
                    self.startDate = start_date;
                    self.endDate = end_date;
                    $('#start_time').val(self.startDate);
                    $('#end_time').val(self.endDate);
                    self.sourceTableData = res.data.data.data;
                }).catch(function (err) {
                    console.log(err);
                    self.$message.error("网络错误，请点击重试按钮");
                    self.loading = false;
                    self.needRetry = true;
                });
            },
            retry() {
                this.needRetry = false;
                this.loading = true;
                this.getSourceTableData();
            },
            // 深拷贝原始数据
            getTableData() {
                return JSON.parse(JSON.stringify(this.sourceTableData));
            },
            pageChange(pageIndex) {
                this.pageIndex = pageIndex;
                this.getTableShowData();
                // console.log(pageIndex)
            },
            pageSizeChange(pageSize) {
                this.pageIndex = 1;
                this.pageSize = pageSize;
                this.getTableShowData()
            },
            sortChange(params) {

                function commonHandler(x) {
                    return x;
                }

                var changed = false;

                for (var k in params) {
                    if ((params[k]).length > 0) {
                        var handler = commonHandler;
                        // if ("quzong_ok" === k || "last_visit" === k || "createdat" === k || "closedate" === k){
                        //     handler = stringToDateTime;
                        // }

                        this.tableData.sort(function (a, b) {
                            var x = handler(a[k]);
                            var y = handler(b[k]);

                            if (x === null || x === undefined || x === "") {
                                return -1;
                            }
                            if (y === null || y === undefined || y === "") {
                                return 1;
                            }

                            if (params[k] === 'asc') {
                                return x - y
                            } else if (params[k] === 'desc') {
                                return y - x
                            } else {
                                return 0
                            }
                        });
                        changed = true;
                    }
                }

                if (changed) {
                    this.pageChange(1);
                }
            },
            _filterMethod(tableData) {
                let filters = this.filters;
                for (let field in filters) {
                    let values = filters[field];
                    if (Array.isArray(values)) {
                        if (field == "XXXXXXXXXXXXXXXXXXX") {
                            tableData = tableData.filter(item => item[field] == values[0]);
                        } else {
                            tableData = tableData.filter(item => values.indexOf(item[field]) > -1);
                        }
                    }
                }
                return tableData;
            },
            filterMethod(filters) {

                this.filters = filters;
                console.log("filters", filters)
                let tableData = this.getTableData();

                tableData = this._filterMethod(tableData);
                tableData = this._searchMethod(tableData);

                this.tableData = tableData;
                this.total = this.tableData.length;
                this.pageChange(1);
                this.resetConditions();
            },
            _searchOnce(tableData, searcher) {

                var searchType = searcher.searchType;
                var columnName = searcher.columnName;
                var start = searcher.start;
                var end = searcher.end;

                if (searchType == "string" || searchType == String) {
                    if (start) {
                        var re = new RegExp(start, "i");
                        tableData = tableData.filter(item => re.test(item[columnName]))
                    }
                }

                if (searchType == "number" || searchType == Number) {

                    tableData = tableData.filter(item => item[columnName] == start)
                }

                if (searchType == "numberRange" || searchType == NumberRange) {

                    if (start != null && start != undefined && start != "") {
                        tableData = tableData.filter(item => item[columnName] >= start)
                    }

                    if (end != null && end != undefined && end != "") {
                        tableData = tableData.filter(item => item[columnName] <= end)
                    }
                }

                if (searchType == "dateRange" || searchType == DateRange) {

                    if (start != null && start != undefined && start != "") {
                        var startDate = stringToDate(start);
                        tableData = tableData.filter(item => stringToDate(item[columnName]) >= startDate)
                    }

                    if (end != null && end != undefined && end != "") {
                        var endDate = stringToDate(end);
                        tableData = tableData.filter(item => stringToDate(item[columnName]) <= endDate)
                    }
                }

                return tableData;
            },

            _searchMethod(tableData) {

                var searchers = this.searchers;
                for (let key in searchers) {
                    let searcher = searchers[key];
                    tableData = this._searchOnce(tableData, searcher);
                }
                return tableData;
            },

            // 关键字、数字、数字范围、时间范围搜索
            searchMethod(searcher) {
                let tableData = this.getTableData();
                console.log("searcher", this.searchers)
                let columnName = searcher.columnName;

                this.searchers[columnName] = searcher;

                tableData = this._filterMethod(tableData);

                tableData = this._searchMethod(tableData);

                this.tableData = tableData;

                this.total = this.tableData.length;
                this.pageChange(1);
                this.resetConditions();
            },
            resetConditions() {
                let self = this;
                self.conditions = {};
                for (let k in self.searchers) {
                    let searcher = self.searchers[k];
                    if (searcher.start || searcher.end) {
                        if (!(self.conditions[k])) {
                            let name = self.tableConfig.columnDict[k];
                            let desc = "";
                            let searchType = searcher.searchType;
                            if (searchType === "string" || searchType === "number") {
                                desc = searcher.start;
                            } else if (searchType === "numberRange" || searchType === "dateRange") {
                                desc = searcher.start + "~" + searcher.end;
                            }
                            if (desc.length > 30) {
                                desc = desc.substr(0, 27) + "...";
                            }
                            self.conditions[k] = name + ":" + desc;
                            console.log("SSSSSSSSSSSSSS", self.conditions[k])
                        }
                    }
                }
                for (let k in self.filters) {
                    let filter = self.filters[k];
                    if (filter && filter.length > 0) {
                        if (!(self.conditions[k])) {
                            let name = self.tableConfig.columnDict[k];
                            let desc = filter.join(",");
                            if (desc.length > 30) {
                                desc = desc.substr(0, 27) + "...";
                            }
                            self.conditions[k] = name + ":" + desc;
                            console.log("FFFFFFFFFFF", self.conditions[k])
                        }
                    }
                }
            },
            // 清空某一列的筛选条件
            removeCondition(k) {
                console.log(this.searchers[k]);
                if (this.searchers[k]) {
                    delete (this.searchers[k]);
                }
                console.log(this.filters[k]);
                if (this.filters[k]) {
                    delete (this.filters[k]);
                }
                // console.log(this.searchers, this.filters);
                // this.resetConditions()
                if ("undefined" == typeof filters) {
                    this.filterMethod();
                } else if ("undefined" == typeof searchers) {
                    this.searchMethod();
                }
                let dropdown = this.getDropdown(k);
                // 重置dropdown里面的筛选条件
                dropdown.rest();
            },
            getDropdown(k) {
                let dropdown = this.$refs["table1"].$refs["dropdown"].find(x => x.columnName === k);
                return dropdown;
            },
            setFooterCellClass(rowIndex, colIndex, value) {
                if (colIndex === 0) {
                    return 'footer-cell-class-name-title'
                } else {
                    return 'footer-cell-class-name-normal'
                }
            },
            // 选择日期插件datepicker
            _datepicker() {
                var date = new Date();
                date.setTime(date.getTime()-24*60*60*1000);
                $('#data_6 .input-daterange').datepicker({
                    keyboardNavigation: false,
                    forceParse: false,
                    autoclose: true,
                    viewDate: new Date(),
                    endDate:date
                });
                $('#data_6 .input-daterange').datepicker("setDate", new Date());
            },

            initTable() {
                this.tableData = this.getTableData();
                this.total = this.tableData.length;
                this.getTableShowData();
                this._datepicker();
                this.loading = false;

            }
        },
        created() {
            this.getSourceTableData();
        },
        watch: {
            "sourceTableData": "initTable",
            // "customerLevelFilters": "setCustomerLevelFilters",
        }
    });
}


