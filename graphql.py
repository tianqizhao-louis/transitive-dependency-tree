import xkcd2347
import os 
from dotenv import load_dotenv


def main():
  load_dotenv()
  gh = xkcd2347.GitHub(key=os.getenv('GITHUB_TOKEN'))
  with open("output.txt", "w", encoding="utf8") as file:
    for dep in gh.get_dependencies(os.getenv('REPO_OWNER'), os.getenv('REPO_NAME'), depth=int(os.getenv('BOUND'))):
      indent = dep['level'] * "    "
      package = dep['packageName']
      # if dep['repository']:
      #     url = 'https://github.com/{0[owner][login]}/{0[name]}'.format(dep['repository'])
      # else:
      #     url = ''
      file.write(f"{indent}{package}\n")
  
  
if __name__ == "__main__":
    main()


# import requests
# import json
# import pandas as pd 

# url = 'https://api.github.com/graphql'

# access_token = "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"

# headers = {"Authorization": f"Bearer {access_token}"}

# query = """
# {
#   repository(owner:"simonw", name:"datasette") {
#     dependencyGraphManifests {
#       totalCount
#       nodes {
#         filename
#       }
#       edges {
#         node {
#           blobPath
#           dependencies {
#             totalCount
#             nodes {
#               packageName
#               requirements
#               hasDependencies
#               packageManager
#             }
#           }
#         }
#       }
#     }
#   }
# }
# """

# r = requests.post(url=url, json={'query': query}, headers=headers)

# print(r)

# # query = """query {
# #     characters {
# #     results {
# #       name
# #       status
# #       species
# #       type
# #       gender
# #     }
# #   }
# # }"""

# # url = 'https://rickandmortyapi.com/graphql/'
# # r = requests.post(url, json={'query': query})
# # json_data = json.loads(r.text)
# # df_data = json_data['data']['characters']['results']
# # df = pd.DataFrame(df_data)

# # print(df)