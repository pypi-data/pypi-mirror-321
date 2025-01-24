#!/usr/bin/env python3

import time
import click
from colorama import Fore, Style
import yaml
import os
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import DoubleQuotedScalarString
from ruamel.yaml.scalarstring import PreservedScalarString
from collections import OrderedDict

@click.group()
def main():
    time.sleep(1)
    colorful_banner("✨ Welcome to make_action ✨")

@main.command()
@click.option('--name', prompt=Fore.CYAN+'🔹 Name of the workflow', help='Name of the workflow to be created.', default="MyWorkflow")
@click.option('--type', prompt=Fore.MAGENTA+'🔹 Which creation type ? (basic, complex)', help='If you choose type Basic some options are not available', default='basic')

def create(name, type):
    
    while type not in ['basic', 'complex']:
        type = input(Fore.MAGENTA + "🔹 Which creation type ? (basic, complex) [basic]: ") or "basic"

        if type in ['basic', 'complex']:
            break
        print(Fore.RED + "❌ Invalid type. Please choose 'basic' or 'complex'.")
    isBasic = type == "basic"     
        
    """Create a new YAML workflow file."""    
    
    github_events = (
        'push',
        'pull_request',
        'pull_request_review',
        'pull_request_review_comment',
        'issues',
        'issue_comment',
        'fork',
        'star',
        'watch',
        'release',
        'deployment',
        'deployment_status',
        'create',
        'delete',
        'workflow_dispatch',
        'schedule',
        'repository_dispatch',
        'status',
        'check_run',
        'check_suite',
        'workflow_run',
        'page_build',
        'project',
        'project_card',
        'project_column',
        'public',
        'member',
        'membership',
        'repository',
        'team',
        'team_add',
        'label',
        'milestone',
        'milestone_status',
        'repository_import',
        'repository_vulnerability_alert',
    )
    
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.default_flow_style = False   
    
    #doc Créer la structure de base du workflow yaml
    workflow = CommentedMap()
    
    
    event_trigger = click.prompt(Fore.GREEN +'🔹 Which trigger event do you want to use (push, pull_request, etc.)', default='push')
    branch_select = click.prompt(Fore.YELLOW +"🔹 On which branch should the event will be trigger ?", default='main')
    
    
    if event_trigger in github_events:
        
        create_yaml(name, event_trigger, workflow, yaml, branch_select, isBasic)
        
        #doc Créer le dossier .github/workflows s'il n'existe pas
        os.makedirs('.github/workflows', exist_ok=True)


        #doc Écrire le fichier YAML
        with open(f'.github/workflows/{name}.yml', 'w') as file:
            yaml.dump(workflow, file)
            
        clear_console()
        colorful_banner(f'''🎉 Workflow {name}.yml successfully created! 🎉''')
    
    else : 
        click.echo("❌ L'évènement GitHub choisi "+ event_trigger +" n'est pas pris en charge.")
        

def create_yaml(name, event_trigger, workflow, yaml, branch_select, isBasic):
    
        workflow['name'] = name
        # Ajouter une ligne vide avant "on"
        workflow.yaml_set_comment_before_after_key('on', before='\n')
        workflow['on'] = CommentedMap()
        workflow['on'][event_trigger] = CommentedMap()
        
        
        #doc Ajouter les branches avec des guillemets doubles
        branches = yaml.seq([DoubleQuotedScalarString(branch_select)])
        branches.fa.set_flow_style()   

        workflow.yaml_set_comment_before_after_key('permissions', before='\n')

        
        workflow['on']['push']['branches'] = branches
        
        managePermissions(workflow, isBasic)
                
        
        workflow.yaml_set_comment_before_after_key('concurrency', before='\n')
        
        #doc oncurrency
        workflow['concurrency'] = CommentedMap()
        workflow['concurrency']["group"] = DoubleQuotedScalarString('pages')
        workflow['concurrency']["cancel-in-progress"] = False
        
        workflow.yaml_set_comment_before_after_key('env', before='\n')
        
        
        resManageEnv = manageENV(workflow, isBasic)
        
        
        workflow.yaml_set_comment_before_after_key('jobs', before='\n')

        workflow['jobs'] = CommentedMap()
        
        manageJobs( workflow , isBasic, resManageEnv)
        
        
        
        

        workflow.yaml_set_comment_before_after_key('name', before='\n')    
            
def manageJobs(workflow, isBasic, envIsCreate):
    
    
    
    isBuild = False
    isDeploy = False
    
    if envIsCreate :
        clear_console()
        banner_text = "🪸  Astro Part 🪸"
        print(Fore.BLUE + Style.BRIGHT + banner_text.center(80) + Style.RESET_ALL + "\n" * 2) 
        needBuild = click.prompt(Fore.MAGENTA +'🔹 Build Astro (yes, no)', default='no')
        if needBuild == 'yes':
            buildAstroConstruction(workflow)  
            isBuild = True
    
    clear_console()
    banner_text = "🚀 Deploy 🚀"
    print(Fore.BLUE + Style.BRIGHT + banner_text.center(80) + Style.RESET_ALL + "\n" * 2) 
    needDeploy = click.prompt(Fore.CYAN +'🔹 Deploy (yes, no)', default='no')
    if needDeploy == 'yes':        
        deployConstruction(workflow, isBuild) 
        isDeploy = True
    
    clear_console()
    banner_text = "📩 Google Notification 📩"
    print(Fore.BLUE + Style.BRIGHT + banner_text.center(80) + Style.RESET_ALL + "\n" * 2)
    needGoogleChat = click.prompt(Fore.YELLOW +'🔹 Google Chat notification (yes, no)', default='no')
    
    if needGoogleChat == 'yes':        
        jobs = []
        if isBuild :
            jobs.append('build')
        if isDeploy: 
            jobs.append('deploy')   
             
        createGoogleChatNotification( workflow, jobs)
        
def createGoogleChatNotification ( workflow, jobs ):
    """ Create Google Notification part with lib SimonScholz/google-chat-action@main"""
    
    
     
    workflow.yaml_set_comment_before_after_key('google_notification', before='\n')
    
    
    workflow['jobs']['google_notification'] = CommentedMap()
    
    if len(jobs) > 0 :
        workflow['jobs']['google_notification']['needs'] = jobs
    
    workflow['jobs']['google_notification']['runs-on'] = 'ubuntu-latest'
    
    useGitHubSecret = click.prompt(Fore.GREEN +'🔹 You wanna use GitHub secret for webhook url ? (yes, no)', default='yes')
    
    webhookUrl = ''
    
    if useGitHubSecret == 'yes' :
        webhookUrl = "${{ secrets.GOOGLE_CHAT_URL }}"
    else :
        
        while webhookUrl == '':
            webhookUrl = click.prompt(Fore.BLUE +'🔹Which webhook url ?')  
       
    
    # workflow['jobs']['google_notification']['steps']['name'] = 'Notify Google Chat'
    # workflow['jobs']['google_notification']['steps']['if'] = '${{ always() }}'
    # workflow['jobs']['google_notification']['steps']['uses'] = 'SimonScholz/google-chat-action@main'
    
    
    
    
    
    # workflow['jobs']['google_notification']['steps']['with'] = CommentedMap()
    
    
              
    # workflow['jobs']['google_notification']['steps']['with']['webhookUrl'] = webhookUrl
    
    title = ""
    while title == "" :       
         
        if len(jobs) > 0 :
            #doc il y a des jobs a verifier
            successMessage = ""
            errorMessage = ""
            
            while successMessage == '':
                successMessage = click.prompt(Fore.CYAN +'🔹 Choose a notification title if success ') 
                
            while errorMessage == '':
                errorMessage = click.prompt(Fore.RED +'🔹 Choose a notification title if there is some errors ')
                
            if 'build' in jobs :
                title = "${{ needs.build.result == 'success'"
                if 'deploy' in jobs : 
                    title = title + " && needs.deploy.result == 'success' && "
            else : 
                title =   "${{ needs.deploy.result == 'success' && " 
            
            title = f"${{{{ needs.build.result == 'success' && needs.deploy.result == 'success' && '{successMessage}' || '{errorMessage}' }}}}"
                 
        else : 
            title = click.prompt(Fore.BLUE +'🔹 Choose a notification title ') 
            
    subtitle = ""
    while subtitle == "" :       
     
        if len(jobs) > 0 :
            #doc il y a des jobs a verifier
            successMessage = ""
            errorMessage = ""
            
            while successMessage == '':
                successMessage =click.prompt(Fore.CYAN +'🔹 Choose a notification subtitle if success ') 
                
            while errorMessage == '':
                errorMessage = click.prompt(Fore.RED +'🔹 Choose a notification subtitle if there is some errors ')
                
            if 'build' in jobs :
                subtitle = "${{ needs.build.result == 'success'"
                if 'deploy' in jobs : 
                    subtitle = subtitle + " && needs.deploy.result == 'success' && "
            else : 
                subtitle =   "${{ needs.deploy.result == 'success' && " 
            
            subtitle = f"${{{{ needs.build.result == 'success' && needs.deploy.result == 'success' && '{successMessage}' || '{errorMessage}' }}}}"
                
        else : 
            subtitle = click.prompt(Fore.CYAN +'🔹Choose a notification subtitle ') 
            
    additionalSections = """
            [
              {
                "header": "Details de la fusion",
                "collapsible": true,
                "widgets": [
                  { "decoratedText": { "text": "- Titre du commit  : ${{ github.event.commits[0].message }}" } },
                  { "decoratedText": { "text": "- Auteur : ${{ github.event.commits[1].author.username }}" } }
                ]
              },
              {
                "header": "Resultats des jobs",
                "collapsible": true,
                "widgets": [
                  { "decoratedText": { "text": "- Build : ${{ needs.build.result }}" } },
                  { "decoratedText": { "text": "- Deployment : ${{ needs.deploy.result }}" } }
                ]
              }
            ]
    """
       
    
    # workflow['jobs']['google_notification']['steps']['with']['subtitle'] = subtitle
    workflow['jobs']['google_notification']['steps'] = []    
    workflow['jobs']['google_notification']['steps'].append({
        "name": "Notify Google Chat",
        "if" : '${{ always() }}',
        "uses" : 'SimonScholz/google-chat-action@main',
        "with": {
            "webhookUrl": webhookUrl,
            "title": title,
            "subtitle": subtitle,
            "additionalSections": additionalSections
        }
    })  
    
def deployConstruction( workflow, build ):    
    """Construct Base from Deploy """  
    
    
    
    service = ""    
    
    while service not in ['github-pages'] :
        service = click.prompt(Fore.GREEN +'🔹 Which service ? (github-pages)', default='github-pages')
    
    stepName = "Deploy to GitHub Pages"
    stepUses = "actions/deploy-pages@v4"
    
    workflow.yaml_set_comment_before_after_key('deploy', before='\n')
    
    workflow['jobs']['deploy'] = CommentedMap()
    workflow['jobs']['deploy']['environment'] = CommentedMap()
    workflow['jobs']['deploy']['environment']['name'] = service
    workflow['jobs']['deploy']['environment']['url'] = '${{ steps.deployment.outputs.page_url }}'
    
    if build :
        workflow['jobs']['deploy']['needs'] = "build"
        
    workflow['jobs']['deploy']['runs-on'] = "ubuntu-latest"
    workflow['jobs']['deploy']['name'] = "Deploy"
    
    
    step = CommentedMap()
    step['name'] = stepName
    step['id'] = "deployment"
    step['uses'] = stepUses
    
    workflow['jobs']['deploy']['steps'] = []
    workflow['jobs']['deploy']['steps'].append(step)
    
    
    
    
    
    
#doc doit forcement avoir le buid path activé !!!!    
def buildAstroConstruction( workflow ):
    """Construct Base from Build with Framework Astro"""  
    buildEnvironnement = 'ubuntu-24.04'
    
    script = '''if [ -f "${{ github.workspace }}/yarn.lock" ]; then
            echo "manager=yarn" >> $GITHUB_OUTPUT
            echo "command=install" >> $GITHUB_OUTPUT
            echo "runner=yarn" >> $GITHUB_OUTPUT
            echo "lockfile=yarn.lock" >> $GITHUB_OUTPUT
            exit 0
          elif [ -f "${{ github.workspace }}/package.json" ]; then
            echo "manager=npm" >> $GITHUB_OUTPUT
            echo "command=ci" >> $GITHUB_OUTPUT
            echo "runner=npx --no-install" >> $GITHUB_OUTPUT
            echo "lockfile=package-lock.json" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Unable to determine package manager"
            exit 1
          fi'''
      
    workflow['jobs']['build'] = CommentedMap()
    workflow['jobs']['build']['name'] = 'Build'
    workflow['jobs']['build']['runs-on'] = buildEnvironnement
    workflow['jobs']['build']['steps'] = [
        CommentedMap({
            'name': 'Checkout code',
            'uses': 'actions/checkout@v4'
        }),
        CommentedMap({
        'name': 'Detect package manager',
        'id': 'detect-package-manager',
        'run': PreservedScalarString(script),
        }),
        CommentedMap({
            'name': 'Setup Node',
            'uses': 'actions/setup-node@v4',
            'with': {
                'node-version': '20',
                'cache': '${{ steps.detect-package-manager.outputs.manager }}',
                'cache-dependency-path': '${{ env.BUILD_PATH }}/${{ steps.detect-package-manager.outputs.lockfile }}'
            }
        }),
        CommentedMap({
            'name': 'Setup Pages',
            'id': 'pages',
            'uses': 'actions/configure-pages@v5'
        }),
        CommentedMap({
            'name': 'Install dependencies',
            'run': r'''${{ steps.detect-package-manager.outputs.manager }} ${{ steps.detect-package-manager.outputs.command }}''',
            'working-directory': r'''${{ env.BUILD_PATH }}'''
        }),
        CommentedMap({
            'name': 'Build with Astro',
            'run': PreservedScalarString(r'''${{ steps.detect-package-manager.outputs.runner }} astro build \
                --site "${{ steps.pages.outputs.origin }}" \
                --base ${{ steps.pages.outputs.base_path }}'''),
            'working-directory': r'''${{ env.BUILD_PATH }}'''
        }),
        CommentedMap({
            'name': 'Upload artifact',
            'uses': 'actions/upload-pages-artifact@v3',
            'with': {
                'path': '''${{ env.BUILD_PATH }}/dist'''
            }
        })
        
        
    ]
    
        
#doc mis en pause avec isBasic == True car certaines permissions sont obligatoires    
def managePermissions( workflow, isBasic ):
    
    isBasic = True
    clear_console()
    banner_text = "👮 Manage Permissions 👮"
    print(Fore.BLUE + Style.BRIGHT + banner_text.center(80) + Style.RESET_ALL + "\n" * 2) 
    contents = "read"
    pages = "write"
    idToken = "write"
    
    if not isBasic:
        #ecrire les permissions
        contents = click.prompt(Fore.GREEN +'🔹 Which permission for contents (none, read, write)', default='none')
        pages = click.prompt(Fore.MAGENTA +'🔹 Which permission for pages (none, read, write)', default='none')
        idToken = click.prompt(Fore.BLUE +'🔹 Which permission for id-token (none,  write)', default='none')   
        
        
    workflow['permissions'] = CommentedMap()
    workflow['permissions']["contents"] = contents
    workflow['permissions']["contents"] = contents
    workflow['permissions']["pages"] = pages
    workflow['permissions']["id-token"] = idToken    
        
def manageENV( workflow, isBasic ):
    clear_console()
    banner_text = "🌿 Manage .ENV 🌿"
    print(Fore.BLUE + Style.BRIGHT + banner_text.center(80) + Style.RESET_ALL + "\n" * 2) 
    if not isBasic:
        #est ce user veux la partie ENV
        userChoice = click.prompt(Fore.GREEN +'🔹 ENV part is needed ? Select "yes" if you need to build your app  (yes, no)', default='no')
        
        if userChoice == 'yes':
            path = click.prompt(Fore.CYAN +'🔹 which path ? (ex ./yourProject/.env)', default='.')
            workflow['env'] = CommentedMap()
            workflow['env']['BUILD_PATH'] = DoubleQuotedScalarString(path)
            return True
        else: return False
    else: 
        workflow['env'] = CommentedMap()
        workflow['env']['BUILD_PATH'] = DoubleQuotedScalarString(".") 
        return True           
            
def clear_console():
    """Efface la console pour un effet propre."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
        
def colorful_banner(text):
    """Welcome to Make File"""
    
    colors = [Fore.GREEN, Fore.MAGENTA, Fore.BLUE]

    for _ in range(1): 
        for color in colors:
            clear_console()
            print(
                color + Style.BRIGHT + text.center(80) + Style.RESET_ALL + "\n" * 2
            )  
            time.sleep(0.3)


if __name__ == '__main__':
    main()