# Copyright (c) AIxBlock, Inc. 

from typing import List

from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.nlp import ConversationalTextToSqlPipeline


def text2sql_tracking_and_print_results(
        test_case, pipelines: List[ConversationalTextToSqlPipeline]):
    for p in pipelines:
        last_sql, history = '', []
        for item in test_case['utterance']:
            case = {
                'utterance': item,
                'history': history,
                'last_sql': last_sql,
                'database_id': test_case['database_id'],
                'local_db_path': test_case['local_db_path']
            }
            results = p(case)
            print({'question': item})
            print(results)
            last_sql = results[OutputKeys.OUTPUT][OutputKeys.TEXT]
            history.append(item)
