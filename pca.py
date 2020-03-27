import json
import os
import pandas as pd

gtmetrix_data = pd.DataFrame(columns=['onload_time', 'first_contentful_paint_time', 'page_elements', 'report_url', 'redirect_duration', 'first_paint_time', 'dom_content_loaded_duration', 'dom_content_loaded_time', 'dom_interactive_time', 'page_bytes', 'page_load_time', 'html_bytes', 'fully_loaded_time', 'html_load_time', 'rum_speed_index', 'yslow_score', 'pagespeed_score', 'backend_duration', 'onload_duration', 'connect_duration', 'date'])

webtracker_data = pd.DataFrame(columns=['minify_total', 'responses_200', 'testStartOffset', 'bytesOut', 'gzip_savings', 'requestsFull',
                   'start_epoch', 'connections', 'bytesOutDoc', 'result', 'basePageSSLTime', 'docTime',
                   'domContentLoadedEventEnd', 'image_savings', 'requestsDoc', 'firstMeaningfulPaint', 'score_cookies',
                   'firstPaint', 'score_cdn', 'cpu.Idle', 'cpu.largestContentfulPaint::Candidate',
                   'optimization_checked', 'image_total', 'score_minify', 'gzip_total', 'responses_404', 'loadTime',
                   'score_combine', 'firstContentfulPaint', 'firstLayout', 'score_etags', 'loadEventStart',
                   'minify_savings', 'score_progressive_jpeg', 'domInteractive', 'score_gzip', 'score_compress',
                   'domContentLoadedEventStart', 'bytesInDoc', 'firstImagePaint', 'score_keep-alive', 'loadEventEnd',
                   'cached', 'score_cache', 'responses_other', 'fullyLoaded', 'requests', 'final_base_page_request',
                   'TTFB', 'bytesIn', 'test_run_time_ms', 'fullyLoadedCPUms',
                   'PerformancePaintTiming.first-contentful-paint', 'date', 'PerformancePaintTiming.first-paint',
                   'domElements', 'fullyLoadedCPUpct', 'domComplete', 'userTime.WPStart', 'userTime.WM_BootstrapStart',
                   'userTime.WM_BootstrapStop', 'userTime.WM_AABStart', 'userTime.WM_AABStop',
                   'userTime.WM_ConsentTestStart', 'userTime.WM_ConsentTestStop', 'userTime.WM_PlayerStart',
                   'userTime.WM_PlayerStop', 'userTime.WM_StatStart', 'userTime.WM_StatStop',
                   'userTime.WM_DeviceUtilsStart', 'userTime.WM_DeviceUtilsStop', 'userTime.WM_GafAPIStart',
                   'userTime.PrebidLoad', 'userTime.WM_GafAPIStop', 'userTime.WPStop', 'userTime.PrebidLoaded',
                   'userTime.VideoApdTime', 'userTime.HubAPILoad', 'userTime.HubAPIReady',
                   'userTime.WM_getMaxZIndexStart', 'userTime.WM_getMaxZIndexStop', 'userTimingMeasure.WPTiming',
                   'userTimingMeasure.WM_BootstrapTiming', 'userTimingMeasure.WM_AABTiming',
                   'userTimingMeasure.WM_ConsentTestTiming', 'userTimingMeasure.WM_PlayerTiming',
                   'userTimingMeasure.WM_StatTiming', 'userTimingMeasure.WM_DeviceUtilsTiming',
                   'userTimingMeasure.WM_GafAPITiming', 'userTimingMeasure.WM_getMaxZIndexTiming', 'userTime',
                   'Colordepth', 'SpeedIndex', 'visualComplete85', 'visualComplete90', 'visualComplete95',
                   'visualComplete99', 'visualComplete', 'render', 'lastVisualChange',
                   'chromeUserTiming.navigationStart', 'chromeUserTiming.fetchStart', 'chromeUserTiming.domLoading',
                   'chromeUserTiming.markAsMainFrame', 'chromeUserTiming.responseEnd', 'chromeUserTiming.firstLayout',
                   'chromeUserTiming.firstPaint', 'chromeUserTiming.firstContentfulPaint',
                   'chromeUserTiming.firstImagePaint', 'chromeUserTiming.LayoutShift',
                   'chromeUserTiming.domInteractive', 'chromeUserTiming.domContentLoadedEventStart',
                   'chromeUserTiming.domContentLoadedEventEnd', 'chromeUserTiming.firstMeaningfulPaintCandidate',
                   'chromeUserTiming.firstMeaningfulPaint', 'chromeUserTiming.domComplete',
                   'chromeUserTiming.loadEventStart', 'chromeUserTiming.loadEventEnd',
                   'chromeUserTiming.LargestImagePaint', 'chromeUserTiming.LargestContentfulPaint',
                   'chromeUserTiming.LargestTextPaint', 'FirstInteractive', 'TTIMeasurementEnd', 'LastInteractive',
                   'FirstCPUIdle', 'run', 'step', 'effectiveBps', 'effectiveBpsDoc', 'domTime', 'aft', 'titleTime',
                   'domLoading', 'server_rtt', 'smallImageCount', 'bigImageCount', 'maybeCaptcha',
                   'heroElementTimes.Image', 'heroElementTimes.Heading', 'heroElementTimes.FirstPaintedHero',
                   'heroElementTimes.LastPaintedHero', 'FirstPaintedHero', 'LastPaintedHero', 'avgRun', 'url', 'location', 'date'])


path_to_json = 'data/'
for subdir, dirs, files in os.walk(path_to_json):
    date = subdir.replace(path_to_json, '')
    print(date)
    for file in files:
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

        # gtmetrix_data has url in column 3 natively
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_json, js)) as json_file:
                json_text = json.load(json_file)
                if 'data' in json_text:
                    # handle webtracker json
                    entry = json_text['data']['average']['firstView']
                    new_data = list()
                    for col in webtracker_data.columns:
                        if col == 'url':
                            new_data.append(json_text['data']['url'])
                        elif col == 'location':
                            new_data.append(json_text['data']['location'])
                        elif col == 'date':
                            new_data.append(date)
                        else:
                            new_data.append(entry[col])
                    webtracker_data.loc[index] = new_data

                else:
                    # handle gtmetrix json
                    entry = json_text['results']
                    new_data = list()
                    for col in gtmetrix_data.columns:
                        if col == 'date':
                            new_data.append(date)
                        else:
                            new_data.append(entry[col])
                    gtmetrix_data.loc[index] = new_data

print(gtmetrix_data)
print(webtracker_data)
# todo: don't pass columns 3 (url) and 6 (null) to PCA for gtmetrix and last two for webtracker (url, location)
#pca = PCA(n_components=3)
#pca.fit(gtmetrix_data)
