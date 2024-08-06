# Object.fromEntries(Object.values(toolMap).map((tool) => Object.entries(tool).map(([toolName, endpoint]) => (endpoint["bestGuess"] === undefined ? [toolName, Object.fromEntries(Object.entries(endpoint).map(([type, { bestGuess }]) => [type, bestGuess]))] : [toolName, endpoint["bestGuess"]]))).flat())

tool_map = {
    "42Crunch": {
        "API": "GET /user/tools/generic/login_details/42Crunch",
        "Push script": "GET /user/tools/generic/configurations/42Crunch/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=42Crunch&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/42Crunch"
    },
    "AWS Security Hub": {
        "API": "GET /user/tools/generic/login_details/AWS%20Security%20Hub",
        "WebHook": "GET /user/tools/generic/configurations/AWS%20Security%20Hub/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/AWS%20Security%20Hub/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=AWS+Security+Hub&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/AWS%20Security%20Hub"
    },
    "Acunetix": {
        "API": "GET /user/tools/generic/login_details/Acunetix",
        "Push script": "GET /user/tools/generic/configurations/Acunetix/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Acunetix&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Acunetix"
    },
    "Amazon GuardDuty": {
        "WebHook": "GET /user/tools/generic/configurations/Amazon%20GuardDuty/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/Amazon%20GuardDuty/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Amazon+GuardDuty&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Amazon%20GuardDuty"
    },
    "Amazon Inspector": {
        "API": "GET /user/tools/generic/login_details/Amazon%20Inspector",
        "WebHook": "GET /user/tools/generic/configurations/Amazon%20Inspector/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/Amazon%20Inspector/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Amazon+Inspector&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Amazon%20Inspector"
    },
    "Apiiro": {
        "API": "GET /user/tools/generic/login_details/Apiiro",
        "Push script": "GET /user/tools/generic/configurations/Apiiro/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Apiiro&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Apiiro"
    },
    "AppCheck": {
        "API": "GET /user/tools/generic/login_details/AppCheck",
        "Push script": "GET /user/tools/generic/configurations/AppCheck/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=AppCheck&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/AppCheck"
    },
    "Appknox": {
        "API": "GET /user/tools/generic/login_details/Appknox",
        "Settings": "GET /user/tools/scheduler/default/Appknox"
    },
    "Appscan": {
        "Push script": "GET /user/tools/generic/configurations/Appscan/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Appscan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Appscan"
    },
    "Aqua": {
        "API": "GET /user/tools/generic/login_details/Aqua",
        "Settings": "GET /user/tools/scheduler/default/Aqua"
    },
    "Avocado": {
        "Push script": "GET /user/tools/generic/configurations/Avocado/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Avocado&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Avocado"
    },
    "Bandit": {
        "Push script": "GET /user/tools/generic/configurations/Bandit/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Bandit&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bandit"
    },
    "BitSight": {
        "API": "GET /user/tools/generic/login_details/BitSight",
        "Push script": "GET /user/tools/generic/configurations/BitSight/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=BitSight&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/BitSight"
    },
    "Blackduck Hub": {
        "API": "GET /user/tools/generic/login_details/Blackduck%20Hub",
        "Push script": "GET /user/tools/generic/configurations/Blackduck%20Hub/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Blackduck+Hub&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Blackduck%20Hub"
    },
    "Blubracket": {
        "API": "GET /user/tools/generic/login_details/Blubracket",
        "Push script": "GET /user/tools/generic/configurations/Blubracket/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Blubracket&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Blubracket"
    },
    "Brakeman": {
        "Push script": "GET /user/tools/generic/configurations/Brakeman/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Brakeman&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Brakeman"
    },
    "Bridgecrew": {
        "API": "GET /user/tools/generic/login_details/Bridgecrew",
        "Push script": "GET /user/tools/generic/configurations/Bridgecrew/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Bridgecrew&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bridgecrew"
    },
    "Bugcrowd": {
        "API": "GET /user/tools/generic/login_details/Bugcrowd",
        "Push script": "GET /user/tools/generic/configurations/Bugcrowd/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Bugcrowd&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bugcrowd"
    },
    "Bundler Audit": {
        "Push script": "GET /user/tools/generic/configurations/Bundler%20Audit/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Bundler+Audit&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bundler%20Audit"
    },
    "Burpsuite Enterprise": {
        "API": "GET /user/tools/generic/login_details/Burpsuite%20Enterprise",
        "Push script": "GET /user/tools/generic/configurations/Burpsuite%20Enterprise/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Burpsuite+Enterprise&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Burpsuite%20Enterprise"
    },
    "Burpsuite": {
        "Push script": "GET /user/tools/generic/configurations/Burpsuite/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Burpsuite&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Burpsuite"
    },
    "Checkmarx One": {
        "API": "GET /user/tools/generic/login_details/Checkmarx%20One",
        "Push script": "GET /user/tools/generic/configurations/Checkmarx%20One/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Checkmarx+One&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Checkmarx%20One"
    },
    "Checkmarx SCA": {
        "API": "GET /user/tools/generic/login_details/Checkmarx%20SCA",
        "Push script": "GET /user/tools/generic/configurations/Checkmarx%20SCA/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Checkmarx+SCA&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Checkmarx%20SCA"
    },
    "Checkmarx": {
        "API": "GET /user/tools/generic/login_details/Checkmarx",
        "Push script": "GET /user/tools/generic/configurations/Checkmarx/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Checkmarx&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Checkmarx"
    },
    "Checkov": {
        "Push script": "GET /user/tools/generic/configurations/Checkov/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Checkov&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Checkov"
    },
    "Clayton": {
        "API": "GET /user/tools/generic/login_details/Clayton",
        "Push script": "GET /user/tools/generic/configurations/Clayton/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Clayton&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Clayton"
    },
    "Cloud Optix": {
        "API": "GET /user/tools/generic/login_details/Cloud%20Optix",
        "Push script": "GET /user/tools/generic/configurations/Cloud%20Optix/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Cloud+Optix&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Cloud%20Optix"
    },
    "Cobalt": {
        "API": "GET /user/tools/generic/login_details/Cobalt",
        "Push script": "GET /user/tools/generic/configurations/Cobalt/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Cobalt&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Cobalt"
    },
    "Contrast Security": {
        "API": "GET /user/tools/generic/login_details/Contrast%20Security",
        "Push script": "GET /user/tools/generic/configurations/Contrast%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Contrast+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Contrast%20Security"
    },
    "Cortex XDR": {
        "API": "GET /user/tools/generic/login_details/Cortex%20XDR",
        "Push script": "GET /user/tools/generic/configurations/Cortex%20XDR/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Cortex+XDR&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Cortex%20XDR"
    },
    "Coverity": {
        "API": "GET /user/tools/generic/login_details/Coverity",
        "Push script": "GET /user/tools/generic/configurations/Coverity/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Coverity&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/coverity/predefined-issue-kinds"
    },
    "CrowdStrike Falcon": {
        "API": "GET /user/tools/generic/login_details/CrowdStrike%20Falcon",
        "Push script": "GET /user/tools/generic/configurations/CrowdStrike%20Falcon/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=CrowdStrike+Falcon&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/CrowdStrike%20Falcon"
    },
    "Custom-AutomationTool": {
        "Push script": "GET /user/tools/generic/configurations/Custom-AutomationTool/?toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Custom-AutomationTool&triggerby=UI_UPLOAD",
        "Fields Mapping": "GET /user/tools/custom/configurations/44",
        "Settings": "GET /user/tools/scheduler/default/Custom-AutomationTool"
    },
    "Custom-Automationsample": {
        "Push script": "GET /user/tools/generic/configurations/Custom-Automationsample/?toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Custom-Automationsample&triggerby=UI_UPLOAD",
        "Fields Mapping": "GET /user/tools/custom/configurations/46",
        "Settings": "GET /user/tools/scheduler/default/Custom-Automationsample"
    },
    "Custom-Sample": {
        "Push script": "GET /user/tools/generic/configurations/Custom-Sample/?toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Custom-Sample&triggerby=UI_UPLOAD",
        "Fields Mapping": "GET /user/tools/custom/configurations/47",
        "Settings": "GET /user/tools/scheduler/default/Custom-Sample"
    },
    "Custom-Test SSDLC": {
        "Push script": "GET /user/tools/generic/configurations/Custom-Test%20SSDLC/?toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Custom-Test+SSDLC&triggerby=UI_UPLOAD",
        "Fields Mapping": "GET /user/tools/custom/configurations/178",
        "Settings": "GET /user/tools/scheduler/default/Custom-Test%20SSDLC"
    },
    "Custom-random": {
        "Push script": "GET /user/tools/generic/configurations/Custom-random/?toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Custom-random&triggerby=UI_UPLOAD",
        "Fields Mapping": "GET /user/tools/custom/configurations/48",
        "Settings": "GET /user/tools/scheduler/default/Custom-random"
    },
    "CycloneDX": {
        "Push script": "GET /user/tools/generic/configurations/CycloneDX/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=CycloneDX&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/CycloneDX"
    },
    "Cycode": {
        "API": "GET /user/tools/generic/login_details/Cycode",
        "Push script": "GET /user/tools/generic/configurations/Cycode/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Cycode&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Cycode"
    },
    "Data Theorem": {
        "API": "GET /user/tools/generic/login_details/Data%20Theorem",
        "Push script": "GET /user/tools/generic/configurations/Data%20Theorem/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Data+Theorem&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Data%20Theorem"
    },
    "Deepfence": {
        "API": "GET /user/tools/generic/login_details/Deepfence",
        "Push script": "GET /user/tools/generic/configurations/Deepfence/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Deepfence&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Deepfence"
    },
    "Dependency Check": {
        "Push script": "GET /user/tools/generic/configurations/Dependency%20Check/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Dependency+Check&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Dependency%20Check"
    },
    "Dependency Track": {
        "API": "GET /user/tools/generic/login_details/Dependency%20Track",
        "Push script": "GET /user/tools/generic/configurations/Dependency%20Track/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Dependency+Track&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Dependency%20Track"
    },
    "Detect Secrets": {
        "Push script": "GET /user/tools/generic/configurations/Detect%20Secrets/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Detect+Secrets&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Detect%20Secrets"
    },
    "Docker Scout": {
        "Push script": "GET /user/tools/generic/configurations/Docker%20Scout/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Docker+Scout&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Docker%20Scout"
    },
    "Edgescan": {
        "API": "GET /user/tools/generic/login_details/Edgescan",
        "Push script": "GET /user/tools/generic/configurations/Edgescan/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Edgescan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Edgescan"
    },
    "Endor Labs": {
        "API": "GET /user/tools/generic/login_details/Endor%20Labs",
        "Push script": "GET /user/tools/generic/configurations/Endor%20Labs/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Endor+Labs&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Endor%20Labs"
    },
    "FiniteState": {
        "API": "GET /user/tools/generic/login_details/FiniteState",
        "Push script": "GET /user/tools/generic/configurations/FiniteState/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=FiniteState&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/FiniteState"
    },
    "Fortify": {
        "API": "GET /user/tools/generic/login_details/Fortify",
        "Push script": "GET /user/tools/generic/configurations/Fortify/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Fortify&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Fortify"
    },
    "GitGuardian": {
        "API": "GET /user/tools/generic/login_details/GitGuardian",
        "Push script": "GET /user/tools/generic/configurations/GitGuardian/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=GitGuardian&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/GitGuardian"
    },
    "GitHub Code Scan": {
        "API": "GET /user/tools/generic/login_details/Github%20Code%20Scan",
        "Push script": "GET /user/tools/generic/configurations/Github%20Code%20Scan/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Github+Code+Scan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Github%20Code%20Scan"
    },
    "GitHub Dependabot": {
        "API": "GET /user/tools/generic/login_details/Dependabot",
        "Push script": "GET /user/tools/generic/configurations/Dependabot/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Dependabot&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tenant-config?configType=SYNC_DEPENDABOT_PRS"
    },
    "GitHub Secret Scan": {
        "API": "GET /user/tools/generic/login_details/Github%20Secret%20Scan",
        "Push script": "GET /user/tools/generic/configurations/Github%20Secret%20Scan/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Github+Secret+Scan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Github%20Secret%20Scan"
    },
    "Gitlab Security": {
        "API": "GET /user/tools/generic/login_details/Gitlab%20Security",
        "Push script": "GET /user/tools/generic/configurations/Gitlab%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Gitlab+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Gitlab%20Security"
    },
    "Gitleaks": {
        "Push script": "GET /user/tools/generic/configurations/Gitleaks/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Gitleaks&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Gitleaks"
    },
    "Google Cloud Registry": {
        "API": "GET /user/tools/generic/login_details/Google%20Cloud%20Registry",
        "Push script": "GET /user/tools/generic/configurations/Google%20Cloud%20Registry/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Google+Cloud+Registry&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Google%20Cloud%20Registry"
    },
    "Google Security Command Center": {
        "API": "GET /user/tools/generic/login_details/Google%20Security%20Command%20Center",
        "Settings": "GET /user/tools/scheduler/default/Google%20Security%20Command%20Center"
    },
    "Gosec Scanner": {
        "Push script": "GET /user/tools/generic/configurations/Gosec%20Scanner/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Gosec+Scanner&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Gosec%20Scanner"
    },
    "Grammatech - CodeSentry": {
        "API": "GET /user/tools/generic/login_details/Grammatech%20-%20CodeSentry",
        "Push script": "GET /user/tools/generic/configurations/Grammatech%20-%20CodeSentry/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Grammatech+-+CodeSentry&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Grammatech%20-%20CodeSentry"
    },
    "Grammatech - CodeSonar": {
        "API": "GET /user/tools/generic/login_details/Grammatech%20-%20CodeSonar",
        "Push script": "GET /user/tools/generic/configurations/Grammatech%20-%20CodeSonar/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Grammatech+-+CodeSonar&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Grammatech%20-%20CodeSonar"
    },
    "Grype": {
        "Push script": "GET /user/tools/generic/configurations/Grype/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Grype&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Grype"
    },
    "HackerOne": {
        "API": "GET /user/tools/generic/login_details/HackerOne",
        "Settings": "GET /user/tools/hackerone/finding-status-mapping-toggle"
    },
    "Halo Security": {
        "API": "GET /user/tools/generic/login_details/Halo%20Security",
        "Push script": "GET /user/tools/generic/configurations/Halo%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Halo+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Halo%20Security"
    },
    "Horizon3.ai NodeZero": {
        "API": "GET /user/tools/generic/login_details/NodeZero",
        "Push script": "GET /user/tools/generic/configurations/NodeZero/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=NodeZero&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/NodeZero"
    },
    "IriusRisk": {
        "API": "GET /user/tools/generic/login_details/IriusRisk",
        "Push script": "GET /user/tools/generic/configurations/IriusRisk/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=IriusRisk&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/IriusRisk"
    },
    "JFrog Xray": {
        "API": "GET /user/tools/generic/login_details/JFrog%20Xray",
        "Push script": "GET /user/tools/generic/configurations/JFrog%20Xray/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=JFrog+Xray&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/JFrog%20Xray"
    },
    "Kics": {
        "Push script": "GET /user/tools/generic/configurations/Kics/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Kics&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Kics"
    },
    "Klocwork": {
        "Push script": "GET /user/tools/generic/configurations/Klocwork/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Klocwork&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Klocwork"
    },
    "LGTM": {
        "Push script": "GET /user/tools/generic/configurations/LGTM/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=LGTM&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/LGTM"
    },
    "Lacework": {
        "API": "GET /user/tools/generic/login_details/Lacework",
        "WebHook": "GET /user/tools/generic/configurations/Lacework/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/Lacework/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Lacework&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Lacework"
    },
    "Legitify": {
        "Push script": "GET /user/tools/generic/configurations/Legitify/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Legitify&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Legitify"
    },
    "Magento": {
        "Push script": "GET /user/tools/generic/configurations/Magento/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Magento&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Magento"
    },
    "Mend": {
        "API": "GET /user/tools/generic/login_details/Mend",
        "Push script": "GET /user/tools/generic/configurations/Mend/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Mend&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Mend"
    },
    "Mend.io": {
        "API": "GET /user/tools/generic/login_details/Mend.io",
        "Push script": "GET /user/tools/generic/configurations/Mend.io/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Mend.io&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Mend.io"
    },
    "Mergebase": {
        "API": "GET /user/tools/generic/login_details/Mergebase",
        "Push script": "GET /user/tools/generic/configurations/Mergebase/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Mergebase&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Mergebase"
    },
    "Metasploit": {
        "Push script": "GET /user/tools/generic/configurations/Metasploit/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Metasploit&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Metasploit"
    },
    "Meterian": {
        "API": "GET /user/tools/generic/login_details/Meterian",
        "Push script": "GET /user/tools/generic/configurations/Meterian/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Meterian&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Meterian"
    },
    "Microsoft Defender for Cloud": {
        "API": "GET /user/tools/generic/login_details/Microsoft%20Defender%20for%20Cloud",
        "Push script": "GET /user/tools/generic/configurations/Microsoft%20Defender%20for%20Cloud/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Microsoft+Defender+for+Cloud&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Microsoft%20Defender%20for%20Cloud"
    },
    "Microsoft Defender for Endpoint": {
        "API": "GET /user/tools/generic/login_details/Microsoft%20Defender%20for%20Endpoint",
        "Push script": "GET /user/tools/generic/configurations/Microsoft%20Defender%20for%20Endpoint/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Microsoft+Defender+for+Endpoint&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Microsoft%20Defender%20for%20Endpoint"
    },
    "Mozilla Observatory": {
        "Push script": "GET /user/tools/generic/configurations/Mozilla%20Observatory/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Mozilla+Observatory&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Mozilla%20Observatory"
    },
    "Nessus": {
        "Push script": "GET /user/tools/generic/configurations/Nessus/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Nessus&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Nessus"
    },
    "Netsparker (Invicti)": {
        "API": "GET /user/tools/generic/login_details/Netsparker",
        "Push script": "GET /user/tools/generic/configurations/Netsparker/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Netsparker&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Netsparker"
    },
    "Nikto": {
        "Push script": "GET /user/tools/generic/configurations/Nikto/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Nikto&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Nikto"
    },
    "Noname": {
        "API": "GET /user/tools/generic/login_details/Noname",
        "Push script": "GET /user/tools/generic/configurations/Noname/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Noname&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Noname"
    },
    "NowSecure": {
        "API": "GET /user/tools/generic/login_details/NowSecure",
        "Push script": "GET /user/tools/generic/configurations/NowSecure/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=NowSecure&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/NowSecure"
    },
    "Orca Security": {
        "API": "GET /user/tools/generic/login_details/Orca%20Security",
        "Push script": "GET /user/tools/generic/configurations/Orca%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Orca+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Orca%20Security"
    },
    "Polaris": {
        "API": "GET /user/tools/generic/login_details/Polaris",
        "Push script": "GET /user/tools/generic/configurations/Polaris/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Polaris&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Polaris"
    },
    "Polyspace": {
        "Push script": "GET /user/tools/generic/configurations/Polyspace/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Polyspace&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Polyspace"
    },
    "Prisma Cloud Redlock": {
        "API": "GET /user/tools/generic/login_details/Prisma%20Cloud%20Redlock",
        "Push script": "GET /user/tools/generic/configurations/Prisma%20Cloud%20Redlock/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Prisma+Cloud+Redlock&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Prisma%20Cloud%20Redlock"
    },
    "Prisma Cloud Twistlock": {
        "API": "GET /user/tools/generic/login_details/Prisma%20Cloud%20Twistlock",
        "Push script": "GET /user/tools/generic/configurations/Prisma%20Cloud%20Twistlock/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Prisma+Cloud+Twistlock&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Prisma%20Cloud%20Twistlock"
    },
    "Probely": {
        "API": "GET /user/tools/generic/login_details/Probely",
        "Push script": "GET /user/tools/generic/configurations/Probely/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Probely&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Probely"
    },
    "Prowler": {
        "Push script": "GET /user/tools/generic/configurations/Prowler/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Prowler&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Prowler"
    },
    "Qualys Infrastructure": {
        "API": "GET /user/tools/generic/login_details/Qualys%20Infrastructure",
        "Push script": "GET /user/tools/generic/configurations/Qualys%20Infrastructure/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Qualys+Infrastructure&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Qualys%20Infrastructure"
    },
    "Qualys WebApp": {
        "API": "GET /user/tools/generic/login_details/Qualys%20WebApp",
        "Push script": "GET /user/tools/generic/configurations/Qualys%20WebApp/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Qualys+WebApp&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Qualys%20WebApp"
    },
    "Qwiet AI": {
        "API": "GET /user/tools/generic/login_details/Qwiet%20AI",
        "Push script": "GET /user/tools/generic/configurations/Qwiet%20AI/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Qwiet+AI&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Qwiet%20AI"
    },
    "Rapid7 Insight": {
        "API": "GET /user/tools/generic/login_details/Rapid7%20Insight",
        "Push script": "GET /user/tools/generic/configurations/Rapid7%20Insight/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Rapid7+Insight&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Rapid7%20Insight"
    },
    "Rapid7 InsightVM": {
        "API": "GET /user/tools/generic/login_details/Rapid7%20InsightVM",
        "Push script": "GET /user/tools/generic/configurations/Rapid7%20InsightVM/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Rapid7+InsightVM&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Rapid7%20InsightVM"
    },
    "Rapid7 nexpose": {
        "API": "GET /user/tools/generic/login_details/Rapid7%20nexpose",
        "Push script": "GET /user/tools/generic/configurations/Rapid7%20nexpose/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Rapid7+nexpose&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Rapid7%20nexpose"
    },
    "Redhat ACS": {
        "API": "GET /user/tools/generic/login_details/Redhat%20ACS",
        "Push script": "GET /user/tools/generic/configurations/Redhat%20ACS/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Redhat+ACS&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Redhat%20ACS"
    },
    "RiskRecon": {
        "API": "GET /user/tools/generic/login_details/RiskRecon",
        "Push script": "GET /user/tools/generic/configurations/RiskRecon/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=RiskRecon&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/RiskRecon"
    },
    "RunZero": {
        "API": "GET /user/tools/generic/login_details/RunZero",
        "Push script": "GET /user/tools/generic/configurations/RunZero/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=RunZero&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/RunZero"
    },
    "SD Elements": {
        "API": "GET /user/tools/generic/login_details/SD%20Elements",
        "Push script": "GET /user/tools/generic/configurations/SD%20Elements/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=SD+Elements&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SD%20Elements"
    },
    "Safety": {
        "Push script": "GET /user/tools/generic/configurations/Safety/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Safety&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Safety"
    },
    "Salt Security": {
        "WebHook": "GET /user/tools/generic/configurations/Salt%20Security/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/Salt%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Salt+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Salt%20Security"
    },
    "Scout Suite": {
        "Push script": "GET /user/tools/generic/configurations/Scout%20Suite/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Scout+Suite&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Scout%20Suite"
    },
    "SecurityScorecard": {
        "API": "GET /user/tools/generic/login_details/SecurityScorecard",
        "Push script": "GET /user/tools/generic/configurations/SecurityScorecard/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=SecurityScorecard&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SecurityScorecard"
    },
    "Seeker": {
        "API": "GET /user/tools/generic/login_details/Seeker",
        "Push script": "GET /user/tools/generic/configurations/Seeker/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Seeker&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Seeker"
    },
    "Semgrep": {
        "API": "GET /user/tools/generic/login_details/Semgrep",
        "Push script": "GET /user/tools/generic/configurations/Semgrep/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Semgrep&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Semgrep"
    },
    "SentinelOne": {
        "API": "GET /user/tools/generic/login_details/SentinelOne",
        "Push script": "GET /user/tools/generic/configurations/SentinelOne/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=SentinelOne&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SentinelOne"
    },
    "Snyk": {
        "API": "GET /user/tools/generic/login_details/Snyk",
        "Push script": "GET /user/tools/generic/configurations/Snyk/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Snyk&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Snyk"
    },
    "SonarQube": {
        "API": "GET /user/tools/generic/login_details/SonarQube",
        "Push script": "GET /user/tools/generic/configurations/SonarQube/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=SonarQube&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/SonarQube"
    },
    "Sonarcloud": {
        "API": "GET /user/tools/generic/login_details/Sonarcloud",
        "Push script": "GET /user/tools/generic/configurations/Sonarcloud/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Sonarcloud&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Sonarcloud"
    },
    "Sonatype Lifecycle": {
        "API": "GET /user/tools/generic/login_details/Sonatype%20Lifecycle",
        "Push script": "GET /user/tools/generic/configurations/Sonatype%20Lifecycle/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Sonatype+Lifecycle&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Sonatype%20Lifecycle"
    },
    "Sonrai Security": {
        "API": "GET /user/tools/generic/login_details/Sonrai%20Security",
        "Push script": "GET /user/tools/generic/configurations/Sonrai%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Sonrai+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Sonrai%20Security"
    },
    "Spectral": {
        "API": "GET /user/tools/generic/login_details/Spectral",
        "Push script": "GET /user/tools/generic/configurations/Spectral/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Spectral&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Spectral"
    },
    "Stackhawk": {
        "API": "GET /user/tools/generic/login_details/Stackhawk",
        "Push script": "GET /user/tools/generic/configurations/Stackhawk/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Stackhawk&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Stackhawk"
    },
    "SysDig": {
        "API": "GET /user/tools/generic/login_details/SysDig",
        "Push script": "GET /user/tools/generic/configurations/SysDig/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=SysDig&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SysDig"
    },
    "Tanium": {
        "API": "GET /user/tools/generic/login_details/Tanium",
        "Push script": "GET /user/tools/generic/configurations/Tanium/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Tanium&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Tanium"
    },
    "Tenable Cloud Security": {
        "API": "GET /user/tools/generic/login_details/Tenable%20Cloud%20Security",
        "Push script": "GET /user/tools/generic/configurations/Tenable%20Cloud%20Security/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Tenable+Cloud+Security&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Tenable%20Cloud%20Security"
    },
    "Tenable Vulnerability Management": {
        "API": "GET /user/tools/generic/login_details/Tenable%20Vulnerability%20Management",
        "Settings": "GET /user/tools/scheduler/default/Tenable%20Vulnerability%20Management"
    },
    "Tenable Webapp": {
        "API": "GET /user/tools/generic/login_details/Tenable%20Webapp",
        "Push script": "GET /user/tools/generic/configurations/Tenable%20Webapp/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Tenable+Webapp&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Tenable%20Webapp"
    },
    "Tenable.sc": {
        "API": "GET /user/tools/generic/login_details/Tenable.sc",
        "Settings": "GET /user/tools/scheduler/default/Tenable.sc"
    },
    "Traceable": {
        "API": "GET /user/tools/generic/login_details/Traceable",
        "Push script": "GET /user/tools/generic/configurations/Traceable/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Traceable&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Traceable"
    },
    "Trivy": {
        "Push script": "GET /user/tools/generic/configurations/Trivy/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Trivy&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Trivy"
    },
    "UpGuard": {
        "API": "GET /user/tools/generic/login_details/UpGuard",
        "Push script": "GET /user/tools/generic/configurations/UpGuard/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=UpGuard&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/UpGuard"
    },
    "VM SecureState": {
        "API": "GET /user/tools/generic/login_details/VM%20SecureState",
        "Push script": "GET /user/tools/generic/configurations/VM%20SecureState/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=VM+SecureState&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/VM%20SecureState"
    },
    "Veracode": {
        "API": "GET /user/tools/generic/login_details/Veracode",
        "Push script": "GET /user/tools/generic/configurations/Veracode/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Veracode&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Veracode"
    },
    "WPScan": {
        "Push script": "GET /user/tools/generic/configurations/WPScan/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=WPScan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/WPScan"
    },
    "Wallarm": {
        "API": "GET /user/tools/generic/login_details/Wallarm",
        "Settings": "GET /user/tools/scheduler/default/Wallarm"
    },
    "Web Inspect": {
        "Push script": "GET /user/tools/generic/configurations/Web%20Inspect/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Web+Inspect&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Web%20Inspect"
    },
    "WhiteHat Sentinel": {
        "API": "GET /user/tools/generic/login_details/WhiteHat%20Sentinel",
        "Push script": "GET /user/tools/generic/configurations/WhiteHat%20Sentinel/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=WhiteHat+Sentinel&triggerby=UI_UPLOAD",
        "Settings": "GET /api/business-unit-setting/toolConfig/WhiteHat%20Sentinel"
    },
    "Wiz": {
        "API": "GET /user/tools/generic/login_details/Wiz",
        "WebHook": "GET /user/tools/generic/configurations/Wiz/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/Wiz/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Wiz&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Wiz"
    },
    "Yarn Audit": {
        "Push script": "GET /user/tools/generic/configurations/Yarn%20Audit/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=Yarn+Audit&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Yarn%20Audit"
    },
    "ZAP": {
        "Push script": "GET /user/tools/generic/configurations/ZAP/?page=0&size=10&toolType=PUSH",
        "Scan upload": "GET /api/scans?findingCounts=NEW&page=0&size=10&sort=createdAt%2Cdesc&tool=ZAP&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/ZAP"
    },
    "AlertConnect": "GET /api/alerts/alert-notification-stats?criticallity=CRITICAL&state=UNREAD",
    "ArmorCode Agent": "GET /api/ac-agent/config/all",
    "ArmorCode API": "GET /user/apikey",
    "Automox": "GET /api/tools/automox/",
    "AWS": "GET /api/awsInfra/accounts",
    "Axonius": "GET /user/tools/generic/login_details/AXONIUS",
    "Azure Board": "GET /user/tickets/jira/configuration/login/AZURE_BOARD",
    "Azure Pipeline": "GET /api/builds/?buildTool=AZURE_PIPELINE&sort=createdAt%2Cdesc&page=0&size=10",
    "Azure Repos": "GET /user/tools/git/gitInstallation/repoType/AZURE_REPOS",
    "Bamboo": "GET /api/builds/?buildTool=BAMBOO&sort=createdAt%2Cdesc&page=0&size=10",
    "Bitbucket": "GET /user/tools/git/gitInstallation/repoType/BITBUCKET",
    "BuildKite": "GET /api/builds/?buildTool=BUILDKITE&sort=createdAt%2Cdesc&page=0&size=10",
    "Checkmarx Codebashing": "GET /api/tenant-config?configType=CHECKMARX_CODEBASHING_TRAINING_CONFIG",
    "Circle CI": "GET /api/builds/?buildTool=CIRCLE_CI&sort=createdAt%2Cdesc&page=0&size=10",
    "Device42": "GET /user/tools/generic/login_details/DEVICE42",
    "Digital.ai Agility": {},
    "Drone": "GET /api/builds/?buildTool=DRONE&sort=createdAt%2Cdesc&page=0&size=10",
    "Email": {},
    "Flashpoint VulnDB": {},
    "FreshService": "GET /user/tickets/jira/configuration/login/FRESHSERVICE",
    "GitHub Actions": "GET /api/builds/?buildTool=GITHUB_ACTIONS&sort=createdAt%2Cdesc&page=0&size=10",
    "GitHub": "GET /user/tools/git/gitInstallation/repoType/GITHUB",
    "GitLab CI": "GET /api/builds/?buildTool=GITLAB_CI&sort=createdAt%2Cdesc&page=0&size=10",
    "GitLab Issues": "GET /user/tickets/jira/configuration/login/GITLAB_ISSUES",
    "GitLab": "GET /user/tools/git/gitInstallation/repoType/GITLAB",
    "Imperva": "GET /api/imperva",
    "Jenkins": "GET /api/builds/?buildTool=JENKINS&sort=createdAt%2Cdesc&page=0&size=10",
    "Jira": "GET /user/tickets/jira/configuration/login/JIRA",
    "LeanIX": "GET /user/tickets/jira/configuration/login/LEAN_IX",
    "MS Teams": "GET /user/tools/msteams/list?scope=BUSINESS_UNIT",
    "PagerDuty": "GET /user/tickets/jira/configuration/login/PAGERDUTY",
    "Rally": "GET /user/tickets/jira/configuration/login/RALLY",
    "Release IQ": "GET /api/builds/?buildTool=RELEASE_IQ&sort=createdAt%2Cdesc&page=0&size=10",
    "Secure Code Warrior": "GET /api/tenant-config?configType=SECURE_CODE_WARRIOR_TRAINING_CONFIG",
    "Service Now": "GET /user/tickets/jira/configuration/login/SERVICE_NOW",
    "Shortcut": "GET /user/tickets/jira/configuration/login/SHORTCUT",
    "Slack": "GET /user/tools/slack/workspace?scope=BUSINESS_UNIT",
    "Team City": "GET /api/builds/?buildTool=TEAM_CITY&sort=createdAt%2Cdesc&page=0&size=10",
    "ThreatConnect": "GET /user/generic/configs/THREAT_CONNECT"
}

# Overrides

tool_map["Email"] = "GET /user/notification/tenant"
tool_map["AlertConnect"] = "GET /user/api/integration"
tool_map["Digital.ai Agility"] = "GET /user/tickets/jira/configuration/login/VERSION_ONE" # "GET /user/tickets/jira/configuration?0=VERSION_ONE"
tool_map["Flashpoint VulnDB"] = "GET /user/generic/configs/FLASH_POINT"

# Aliases

tool_map["APIKEY"] = tool_map["ArmorCode API"]
tool_map["ARMORCODE_AGENT"] = tool_map["ArmorCode Agent"]
tool_map["AZURE_REPOS"] = tool_map["Azure Repos"]
tool_map["Dependabot"] = tool_map["GitHub Dependabot"]
tool_map["FLASH_POINT"] = tool_map["Flashpoint VulnDB"]
tool_map["JFrog Vision (Vdoo)"] = tool_map["JFrog Xray"]
tool_map["LEAN_IX"] = tool_map["LeanIX"]
tool_map["MS_Teams"] = tool_map["MS Teams"]
tool_map["Netsparker"] = tool_map["Netsparker (Invicti)"]
tool_map["NodeZero"] = tool_map["Horizon3.ai NodeZero"]
tool_map["Tenable Infrastructure"] = tool_map["Tenable Vulnerability Management"]
tool_map["VERSION_ONE"] = tool_map["Digital.ai Agility"]
