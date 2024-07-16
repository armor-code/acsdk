# Object.fromEntries(Object.values(toolMap).map((tool) => Object.entries(tool).map(([toolName, endpoint]) => (endpoint["bestGuess"] === undefined ? [toolName, Object.fromEntries(Object.entries(endpoint).map(([type, { bestGuess }]) => [type, bestGuess]))] : [toolName, endpoint["bestGuess"]]))).flat())

tool_map = {
    "Snyk": {
        "API": "GET /user/tools/generic/login_details/Snyk",
        "Push script": "GET /user/tools/generic/configurations/filters/Snyk/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Snyk&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Snyk"
    },
    "42Crunch": {
        "API": "GET /user/tools/generic/login_details/42Crunch",
        "Push script": "GET /user/tools/generic/configurations/filters/42Crunch/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=42Crunch&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/42Crunch"
    },
    "AWS Security Hub": {
        "WebHook": "GET /user/tools/generic/configurations/AWS%20Security%20Hub/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/filters/AWS%20Security%20Hub/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/AWS%20Security%20Hub/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/AWS%20Security%20Hub"
    },
    "Acunetix": {
        "API": "GET /user/tools/generic/login_details/Acunetix",
        "Push script": "GET /user/tools/generic/configurations/filters/Acunetix/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Acunetix&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Acunetix"
    },
    "Amazon GuardDuty": {
        "WebHook": "GET /user/tools/generic/configurations/Amazon%20GuardDuty/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/filters/Amazon%20GuardDuty/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Amazon%20GuardDuty/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Amazon%20GuardDuty"
    },
    "Amazon Inspector": {
        "API": "GET /user/tools/generic/login_details/Amazon%20Inspector",
        "WebHook": "GET /user/tools/generic/configurations/Amazon%20Inspector/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/filters/Amazon%20Inspector/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Amazon%20Inspector/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Amazon%20Inspector"
    },
    "Apiiro": {
        "API": "GET /user/tools/generic/login_details/Apiiro",
        "Push script": "GET /user/tools/generic/configurations/filters/Apiiro/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Apiiro&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Apiiro"
    },
    "AppCheck": {
        "API": "GET /user/tools/generic/login_details/AppCheck",
        "Push script": "GET /user/tools/generic/configurations/filters/AppCheck/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=AppCheck&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/AppCheck"
    },
    "Appknox": {
        "API": "GET /user/tools/generic/login_details/Appknox",
        "Settings": "GET /user/tools/scheduler/default/Appknox"
    },
    "Appscan": {
        "Push script": "GET /user/tools/generic/configurations/filters/Appscan/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Appscan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Appscan"
    },
    "Aqua": {
        "API": "GET /user/tools/generic/login_details/Aqua",
        "Settings": "GET /user/tools/scheduler/default/Aqua"
    },
    "Avocado": {
        "Push script": "GET /user/tools/generic/configurations/filters/Avocado/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Avocado&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Avocado"
    },
    "Bandit": {
        "Push script": "GET /user/tools/generic/configurations/filters/Bandit/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Bandit&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bandit"
    },
    "BitSight": {
        "API": "GET /user/tools/generic/login_details/BitSight",
        "Push script": "GET /user/tools/generic/configurations/filters/BitSight/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=BitSight&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/BitSight"
    },
    "Blackduck Hub": {
        "API": "GET /user/tools/generic/login_details/Blackduck%20Hub",
        "Push script": "GET /user/tools/generic/configurations/filters/Blackduck%20Hub/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Blackduck%20Hub/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /api/tool-settings/Blackduck%20Hub"
    },
    "Blubracket": {
        "API": "GET /user/tools/generic/login_details/Blubracket",
        "Push script": "GET /user/tools/generic/configurations/filters/Blubracket/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Blubracket&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Blubracket"
    },
    "Brakeman": {
        "Push script": "GET /user/tools/generic/configurations/filters/Brakeman/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Brakeman&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Brakeman"
    },
    "Bridgecrew": {
        "API": "GET /user/tools/generic/login_details/Bridgecrew",
        "Push script": "GET /user/tools/generic/configurations/filters/Bridgecrew/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Bridgecrew&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bridgecrew"
    },
    "Bugcrowd": {
        "API": "GET /user/tools/generic/login_details/Bugcrowd",
        "Push script": "GET /user/tools/generic/configurations/filters/Bugcrowd/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Bugcrowd&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Bugcrowd"
    },
    "Bundler Audit": {
        "Push script": "GET /user/tools/generic/configurations/filters/Bundler%20Audit/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Bundler%20Audit/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Bundler%20Audit"
    },
    "Burpsuite": {
        "Push script": "GET /user/tools/generic/configurations/filters/Burpsuite/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Burpsuite&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Burpsuite"
    },
    "Burpsuite Enterprise": {
        "API": "GET /user/tools/generic/login_details/Burpsuite%20Enterprise",
        "Push script": "GET /user/tools/generic/configurations/filters/Burpsuite%20Enterprise/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Burpsuite%20Enterprise/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Burpsuite%20Enterprise"
    },
    "Checkmarx": {
        "API": "GET /user/tools/generic/login_details/Checkmarx",
        "Push script": "GET /user/tools/generic/configurations/filters/Checkmarx/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Checkmarx&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Checkmarx"
    },
    "Checkmarx One": {
        "API": "GET /user/tools/generic/login_details/Checkmarx%20One",
        "Push script": "GET /user/tools/generic/configurations/filters/Checkmarx%20One/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Checkmarx%20One/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Checkmarx%20One"
    },
    "Checkmarx SCA": {
        "API": "GET /user/tools/generic/login_details/Checkmarx%20SCA",
        "Push script": "GET /user/tools/generic/configurations/filters/Checkmarx%20SCA/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Checkmarx%20SCA/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Checkmarx%20SCA"
    },
    "Checkov": {
        "Push script": "GET /user/tools/generic/configurations/filters/Checkov/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Checkov&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Checkov"
    },
    "Clayton": {
        "API": "GET /user/tools/generic/login_details/Clayton",
        "Push script": "GET /user/tools/generic/configurations/filters/Clayton/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Clayton&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Clayton"
    },
    "Cloud Optix": {
        "API": "GET /user/tools/generic/login_details/Cloud%20Optix",
        "Push script": "GET /user/tools/generic/configurations/filters/Cloud%20Optix/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Cloud%20Optix/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Cloud%20Optix"
    },
    "Cobalt": {
        "API": "GET /user/tools/generic/login_details/Cobalt",
        "Push script": "GET /user/tools/generic/configurations/filters/Cobalt/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Cobalt&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Cobalt"
    },
    "Contrast Security": {
        "API": "GET /user/tools/generic/login_details/Contrast%20Security",
        "Push script": "GET /user/tools/generic/configurations/filters/Contrast%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Contrast%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Contrast%20Security"
    },
    "Cortex XDR": {
        "API": "GET /user/tools/generic/login_details/Cortex%20XDR",
        "Push script": "GET /user/tools/generic/configurations/filters/Cortex%20XDR/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Cortex%20XDR/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Cortex%20XDR"
    },
    "Coverity": {
        "API": "GET /user/tools/generic/login_details/Coverity",
        "Push script": "GET /user/tools/generic/configurations/filters/Coverity/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Coverity&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/coverity/predefined-issue-kinds"
    },
    "CrowdStrike Falcon": {
        "API": "GET /user/tools/generic/login_details/CrowdStrike%20Falcon",
        "Push script": "GET /user/tools/generic/configurations/filters/CrowdStrike%20Falcon/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/CrowdStrike%20Falcon/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/CrowdStrike%20Falcon"
    },
    "CycloneDX": {
        "Push script": "GET /user/tools/generic/configurations/filters/CycloneDX/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=CycloneDX&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/CycloneDX"
    },
    "Cycode": {
        "API": "GET /user/tools/generic/login_details/Cycode",
        "Push script": "GET /user/tools/generic/configurations/filters/Cycode/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Cycode&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Cycode"
    },
    "Data Theorem": {
        "API": "GET /user/tools/generic/login_details/Data%20Theorem",
        "Push script": "GET /user/tools/generic/configurations/filters/Data%20Theorem/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Data%20Theorem/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Data%20Theorem"
    },
    "Deepfence": {
        "API": "GET /user/tools/generic/login_details/Deepfence",
        "Push script": "GET /user/tools/generic/configurations/filters/Deepfence/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Deepfence&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Deepfence"
    },
    "Dependency Check": {
        "Push script": "GET /user/tools/generic/configurations/filters/Dependency%20Check/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Dependency%20Check/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Dependency%20Check"
    },
    "Dependency Track": {
        "Push script": "GET /user/tools/generic/configurations/filters/Dependency%20Track/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Dependency%20Track/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Dependency%20Track"
    },
    "Detect Secrets": {
        "Push script": "GET /user/tools/generic/configurations/filters/Detect%20Secrets/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Detect%20Secrets/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Detect%20Secrets"
    },
    "Docker Scout": {
        "Push script": "GET /user/tools/generic/configurations/filters/Docker%20Scout/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Docker%20Scout/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Docker%20Scout"
    },
    "Edgescan": {
        "API": "GET /user/tools/generic/login_details/Edgescan",
        "Push script": "GET /user/tools/generic/configurations/filters/Edgescan/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Edgescan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Edgescan"
    },
    "Endor Labs": {
        "API": "GET /user/tools/generic/login_details/Endor%20Labs",
        "Push script": "GET /user/tools/generic/configurations/filters/Endor%20Labs/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Endor%20Labs/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Endor%20Labs"
    },
    "FiniteState": {
        "API": "GET /user/tools/generic/login_details/FiniteState",
        "Push script": "GET /user/tools/generic/configurations/filters/FiniteState/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=FiniteState&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/FiniteState"
    },
    "Fortify": {
        "API": "GET /user/tools/generic/login_details/Fortify",
        "Push script": "GET /user/tools/generic/configurations/filters/Fortify/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Fortify&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Fortify"
    },
    "GitGuardian": {
        "API": "GET /user/tools/generic/login_details/GitGuardian",
        "Push script": "GET /user/tools/generic/configurations/filters/GitGuardian/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=GitGuardian&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/GitGuardian"
    },
    "GitHub Code Scan": {
        "API": "GET /user/tools/generic/login_details/Github%20Code%20Scan",
        "Push script": "GET /user/tools/generic/configurations/filters/Github%20Code%20Scan/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Github%20Code%20Scan/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Github%20Code%20Scan"
    },
    "GitHub Dependabot": {
        "API": "GET /user/tools/generic/login_details/Dependabot",
        "Push script": "GET /user/tools/generic/configurations/filters/Dependabot/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Dependabot&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tenant-config?configType=SYNC_DEPENDABOT_PRS"
    },
    "GitHub Secret Scan": {
        "API": "GET /user/tools/generic/login_details/Github%20Secret%20Scan",
        "Push script": "GET /user/tools/generic/configurations/filters/Github%20Secret%20Scan/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Github%20Secret%20Scan/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Github%20Secret%20Scan"
    },
    "Gitlab Security": {
        "API": "GET /user/tools/generic/login_details/Gitlab%20Security",
        "Push script": "GET /user/tools/generic/configurations/filters/Gitlab%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Gitlab%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Gitlab%20Security"
    },
    "Gitleaks": {
        "Push script": "GET /user/tools/generic/configurations/filters/Gitleaks/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Gitleaks&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Gitleaks"
    },
    "Google Cloud Registry": {
        "API": "GET /user/tools/generic/login_details/Google%20Cloud%20Registry",
        "Push script": "GET /user/tools/generic/configurations/filters/Google%20Cloud%20Registry/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Google%20Cloud%20Registry/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Google%20Cloud%20Registry"
    },
    "Google Security Command Center": {
        "API": "GET /user/tools/generic/login_details/Google%20Security%20Command%20Center",
        "Settings": "GET /user/tools/scheduler/default/Google%20Security%20Command%20Center"
    },
    "Gosec Scanner": {
        "Push script": "GET /user/tools/generic/configurations/filters/Gosec%20Scanner/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Gosec%20Scanner/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Gosec%20Scanner"
    },
    "Grammatech - CodeSentry": {
        "API": "GET /user/tools/generic/login_details/Grammatech%20-%20CodeSentry",
        "Push script": "GET /user/tools/generic/configurations/filters/Grammatech%20-%20CodeSentry/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Grammatech%20-%20CodeSentry/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Grammatech%20-%20CodeSentry"
    },
    "Grammatech - CodeSonar": {
        "API": "GET /user/tools/generic/login_details/Grammatech%20-%20CodeSonar",
        "Push script": "GET /user/tools/generic/configurations/filters/Grammatech%20-%20CodeSonar/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Grammatech%20-%20CodeSonar/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Grammatech%20-%20CodeSonar"
    },
    "Grype": {
        "Push script": "GET /user/tools/generic/configurations/filters/Grype/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Grype&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Grype"
    },
    "HackerOne": {
        "API": "GET /user/tools/generic/login_details/HackerOne",
        "Settings": "GET /user/tools/hackerone/finding-status-mapping-toggle"
    },
    "Halo Security": {
        "API": "GET /user/tools/generic/login_details/Halo%20Security",
        "Push script": "GET /user/tools/generic/configurations/filters/Halo%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Halo%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Halo%20Security"
    },
    "Horizon3.ai NodeZero": {
        "API": "GET /user/tools/generic/login_details/NodeZero",
        "Push script": "GET /user/tools/generic/configurations/filters/NodeZero/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=NodeZero&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/NodeZero"
    },
    "IriusRisk": {
        "API": "GET /user/tools/generic/login_details/IriusRisk",
        "Push script": "GET /user/tools/generic/configurations/filters/IriusRisk/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=IriusRisk&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/IriusRisk"
    },
    "JFrog Xray": {
        "API": "GET /user/tools/generic/login_details/JFrog%20Xray",
        "Push script": "GET /user/tools/generic/configurations/filters/JFrog%20Xray/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/JFrog%20Xray/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/JFrog%20Xray"
    },
    "Kics": {
        "Push script": "GET /user/tools/generic/configurations/filters/Kics/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Kics&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Kics"
    },
    "Klocwork": {
        "Push script": "GET /user/tools/generic/configurations/filters/Klocwork/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Klocwork&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Klocwork"
    },
    "LGTM": {
        "Push script": "GET /user/tools/generic/configurations/filters/LGTM/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=LGTM&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/LGTM"
    },
    "Lacework": {
        "API": "GET /user/tools/generic/login_details/Lacework",
        "WebHook": "GET /user/tools/generic/configurations/Lacework/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/filters/Lacework/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Lacework&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Lacework"
    },
    "Legitify": {
        "Push script": "GET /user/tools/generic/configurations/filters/Legitify/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Legitify&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Legitify"
    },
    "Magento": {
        "Push script": "GET /user/tools/generic/configurations/filters/Magento/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Magento&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Magento"
    },
    "Mend": {
        "API": "GET /user/tools/generic/login_details/Mend",
        "Push script": "GET /user/tools/generic/configurations/filters/Mend/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Mend&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/Mend"
    },
    "Mend.io": {
        "API": "GET /user/tools/generic/login_details/Mend.io",
        "Push script": "GET /user/tools/generic/configurations/filters/Mend.io/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Mend.io&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Mend.io"
    },
    "Mergebase": {
        "API": "GET /user/tools/generic/login_details/Mergebase",
        "Push script": "GET /user/tools/generic/configurations/filters/Mergebase/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Mergebase&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Mergebase"
    },
    "Metasploit": {
        "Push script": "GET /user/tools/generic/configurations/filters/Metasploit/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Metasploit&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Metasploit"
    },
    "Meterian": {
        "API": "GET /user/tools/generic/login_details/Meterian",
        "Push script": "GET /user/tools/generic/configurations/filters/Meterian/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Meterian&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Meterian"
    },
    "Microsoft Defender for Cloud": {
        "API": "GET /user/tools/generic/login_details/Microsoft%20Defender%20for%20Cloud",
        "Push script": "GET /user/tools/generic/configurations/filters/Microsoft%20Defender%20for%20Cloud/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Microsoft%20Defender%20for%20Cloud/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Microsoft%20Defender%20for%20Cloud"
    },
    "Microsoft Defender for Endpoint": {
        "API": "GET /user/tools/generic/login_details/Microsoft%20Defender%20for%20Endpoint",
        "Push script": "GET /user/tools/generic/configurations/filters/Microsoft%20Defender%20for%20Endpoint/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Microsoft%20Defender%20for%20Endpoint/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Microsoft%20Defender%20for%20Endpoint"
    },
    "Mozilla Observatory": {
        "Push script": "GET /user/tools/generic/configurations/filters/Mozilla%20Observatory/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Mozilla%20Observatory/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Mozilla%20Observatory"
    },
    "Nessus": {
        "Push script": "GET /user/tools/generic/configurations/filters/Nessus/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Nessus&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Nessus"
    },
    "Netsparker (Invicti)": {
        "API": "GET /user/tools/generic/login_details/Netsparker",
        "Push script": "GET /user/tools/generic/configurations/filters/Netsparker/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Netsparker&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Netsparker"
    },
    "Nikto": {
        "Push script": "GET /user/tools/generic/configurations/filters/Nikto/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Nikto&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Nikto"
    },
    "Noname": {
        "API": "GET /user/tools/generic/login_details/Noname",
        "Push script": "GET /user/tools/generic/configurations/filters/Noname/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Noname&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Noname"
    },
    "NowSecure": {
        "API": "GET /user/tools/generic/login_details/NowSecure",
        "Push script": "GET /user/tools/generic/configurations/filters/NowSecure/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=NowSecure&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/NowSecure"
    },
    "Orca Security": {
        "API": "GET /user/tools/generic/login_details/Orca%20Security",
        "Push script": "GET /user/tools/generic/configurations/filters/Orca%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Orca%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Orca%20Security"
    },
    "Polaris": {
        "API": "GET /user/tools/generic/login_details/Polaris",
        "Push script": "GET /user/tools/generic/configurations/filters/Polaris/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Polaris&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Polaris"
    },
    "Polyspace": {
        "Push script": "GET /user/tools/generic/configurations/filters/Polyspace/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Polyspace&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Polyspace"
    },
    "Prisma Cloud Redlock": {
        "API": "GET /user/tools/generic/login_details/Prisma%20Cloud%20Redlock",
        "Push script": "GET /user/tools/generic/configurations/filters/Prisma%20Cloud%20Redlock/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Prisma%20Cloud%20Redlock/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /api/tool-settings/Prisma%20Cloud%20Redlock"
    },
    "Prisma Cloud Twistlock": {
        "API": "GET /user/tools/generic/login_details/Prisma%20Cloud%20Twistlock",
        "Push script": "GET /user/tools/generic/configurations/filters/Prisma%20Cloud%20Twistlock/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Prisma%20Cloud%20Twistlock/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Prisma%20Cloud%20Twistlock"
    },
    "Probely": {
        "API": "GET /user/tools/generic/login_details/Probely",
        "Push script": "GET /user/tools/generic/configurations/filters/Probely/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Probely&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Probely"
    },
    "Prowler": {
        "Push script": "GET /user/tools/generic/configurations/filters/Prowler/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Prowler&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Prowler"
    },
    "Qualys Infrastructure": {
        "API": "GET /user/tools/generic/login_details/Qualys%20Infrastructure",
        "Push script": "GET /user/tools/generic/configurations/filters/Qualys%20Infrastructure/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Qualys%20Infrastructure/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Qualys%20Infrastructure"
    },
    "Qualys WebApp": {
        "API": "GET /user/tools/generic/login_details/Qualys%20WebApp",
        "Push script": "GET /user/tools/generic/configurations/filters/Qualys%20WebApp/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Qualys%20WebApp/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Qualys%20WebApp"
    },
    "Qwiet AI": {
        "API": "GET /user/tools/generic/login_details/Qwiet%20AI",
        "Push script": "GET /user/tools/generic/configurations/filters/Qwiet%20AI/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Qwiet%20AI/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Qwiet%20AI"
    },
    "Rapid7 Insight": {
        "API": "GET /user/tools/generic/login_details/Rapid7%20Insight",
        "Push script": "GET /user/tools/generic/configurations/filters/Rapid7%20Insight/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Rapid7%20Insight/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Rapid7%20Insight"
    },
    "Rapid7 InsightVM": {
        "API": "GET /user/tools/generic/login_details/Rapid7%20InsightVM",
        "Push script": "GET /user/tools/generic/configurations/filters/Rapid7%20InsightVM/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Rapid7%20InsightVM/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Rapid7%20InsightVM"
    },
    "Rapid7 nexpose": {
        "API": "GET /user/tools/generic/login_details/Rapid7%20nexpose",
        "Push script": "GET /user/tools/generic/configurations/filters/Rapid7%20nexpose/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Rapid7%20nexpose/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Rapid7%20nexpose"
    },
    "Redhat ACS": {
        "API": "GET /user/tools/generic/login_details/Redhat%20ACS",
        "Push script": "GET /user/tools/generic/configurations/filters/Redhat%20ACS/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Redhat%20ACS/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Redhat%20ACS"
    },
    "RunZero": {
        "API": "GET /user/tools/generic/login_details/RunZero",
        "Push script": "GET /user/tools/generic/configurations/filters/RunZero/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=RunZero&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/RunZero"
    },
    "SD Elements": {
        "API": "GET /user/tools/generic/login_details/SD%20Elements",
        "Push script": "GET /user/tools/generic/configurations/filters/SD%20Elements/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/SD%20Elements/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/SD%20Elements"
    },
    "Safety": {
        "Push script": "GET /user/tools/generic/configurations/filters/Safety/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Safety&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Safety"
    },
    "Salt Security": {
        "WebHook": "GET /user/tools/generic/configurations/Salt%20Security/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/filters/Salt%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Salt%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Salt%20Security"
    },
    "Scout Suite": {
        "Push script": "GET /user/tools/generic/configurations/filters/Scout%20Suite/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Scout%20Suite/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Scout%20Suite"
    },
    "SecurityScorecard": {
        "API": "GET /user/tools/generic/login_details/SecurityScorecard",
        "Push script": "GET /user/tools/generic/configurations/filters/SecurityScorecard/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=SecurityScorecard&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SecurityScorecard"
    },
    "Seeker": {
        "API": "GET /user/tools/generic/login_details/Seeker",
        "Push script": "GET /user/tools/generic/configurations/filters/Seeker/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Seeker&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Seeker"
    },
    "Semgrep": {
        "API": "GET /user/tools/generic/login_details/Semgrep",
        "Push script": "GET /user/tools/generic/configurations/filters/Semgrep/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Semgrep&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Semgrep"
    },
    "SentinelOne": {
        "API": "GET /user/tools/generic/login_details/SentinelOne",
        "Push script": "GET /user/tools/generic/configurations/filters/SentinelOne/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=SentinelOne&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SentinelOne"
    },
    "SonarQube": {
        "API": "GET /user/tools/generic/login_details/SonarQube",
        "Push script": "GET /user/tools/generic/configurations/filters/SonarQube/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=SonarQube&triggerby=UI_UPLOAD",
        "Settings": "GET /api/tool-settings/SonarQube"
    },
    "Sonarcloud": {
        "API": "GET /user/tools/generic/login_details/Sonarcloud",
        "Push script": "GET /user/tools/generic/configurations/filters/Sonarcloud/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Sonarcloud&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Sonarcloud"
    },
    "Sonatype Lifecycle": {
        "API": "GET /user/tools/generic/login_details/Sonatype%20Lifecycle",
        "Push script": "GET /user/tools/generic/configurations/filters/Sonatype%20Lifecycle/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Sonatype%20Lifecycle/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Sonatype%20Lifecycle"
    },
    "Sonrai Security": {
        "API": "GET /user/tools/generic/login_details/Sonrai%20Security",
        "Push script": "GET /user/tools/generic/configurations/filters/Sonrai%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Sonrai%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Sonrai%20Security"
    },
    "Spectral": {
        "API": "GET /user/tools/generic/login_details/Spectral",
        "Push script": "GET /user/tools/generic/configurations/filters/Spectral/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Spectral&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Spectral"
    },
    "Stackhawk": {
        "API": "GET /user/tools/generic/login_details/Stackhawk",
        "Push script": "GET /user/tools/generic/configurations/filters/Stackhawk/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Stackhawk&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Stackhawk"
    },
    "SysDig": {
        "API": "GET /user/tools/generic/login_details/SysDig",
        "Push script": "GET /user/tools/generic/configurations/filters/SysDig/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=SysDig&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/SysDig"
    },
    "Tanium": {
        "API": "GET /user/tools/generic/login_details/Tanium",
        "Push script": "GET /user/tools/generic/configurations/filters/Tanium/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Tanium&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Tanium"
    },
    "Tenable Cloud Security": {
        "API": "GET /user/tools/generic/login_details/Tenable%20Cloud%20Security",
        "Push script": "GET /user/tools/generic/configurations/filters/Tenable%20Cloud%20Security/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Tenable%20Cloud%20Security/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Tenable%20Cloud%20Security"
    },
    "Tenable Vulnerability Management": {
        "API": "GET /user/tools/generic/login_details/Tenable%20Vulnerability%20Management",
        "Settings": "GET /user/tools/scheduler/default/Tenable%20Vulnerability%20Management"
    },
    "Tenable Webapp": {
        "API": "GET /user/tools/generic/login_details/Tenable%20Webapp",
        "Push script": "GET /user/tools/generic/configurations/filters/Tenable%20Webapp/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Tenable%20Webapp/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Tenable%20Webapp"
    },
    "Tenable.sc": {
        "API": "GET /user/tools/generic/login_details/Tenable.sc",
        "Settings": "GET /user/tools/scheduler/default/Tenable.sc"
    },
    "Traceable": {
        "API": "GET /user/tools/generic/login_details/Traceable",
        "Push script": "GET /user/tools/generic/configurations/filters/Traceable/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Traceable&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Traceable"
    },
    "Trivy": {
        "Push script": "GET /user/tools/generic/configurations/filters/Trivy/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Trivy&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Trivy"
    },
    "VM SecureState": {
        "API": "GET /user/tools/generic/login_details/VM%20SecureState",
        "Push script": "GET /user/tools/generic/configurations/filters/VM%20SecureState/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/VM%20SecureState/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/VM%20SecureState"
    },
    "Veracode": {
        "API": "GET /user/tools/generic/login_details/Veracode",
        "Push script": "GET /user/tools/generic/configurations/filters/Veracode/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Veracode&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Veracode"
    },
    "WPScan": {
        "Push script": "GET /user/tools/generic/configurations/filters/WPScan/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=WPScan&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/WPScan"
    },
    "Wallarm": {
        "API": "GET /user/tools/generic/login_details/Wallarm",
        "Settings": "GET /user/tools/scheduler/default/Wallarm"
    },
    "Web Inspect": {
        "Push script": "GET /user/tools/generic/configurations/filters/Web%20Inspect/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Web%20Inspect/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Web%20Inspect"
    },
    "WhiteHat Sentinel": {
        "API": "GET /user/tools/generic/login_details/WhiteHat%20Sentinel",
        "Push script": "GET /user/tools/generic/configurations/filters/WhiteHat%20Sentinel/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/WhiteHat%20Sentinel/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /api/business-unit-setting/toolConfig/WhiteHat%20Sentinel"
    },
    "Wiz": {
        "API": "GET /user/tools/generic/login_details/Wiz",
        "WebHook": "GET /user/tools/generic/configurations/Wiz/?toolType=WEBHOOK",
        "Push script": "GET /user/tools/generic/configurations/filters/Wiz/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=Wiz&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/Wiz"
    },
    "Yarn Audit": {
        "Push script": "GET /user/tools/generic/configurations/filters/Yarn%20Audit/?toolType=PUSH",
        "Scan upload": "GET /user/tools/generic/configurations/Yarn%20Audit/?page=0&size=10&toolType=PUSH",
        "Settings": "GET /user/tools/scheduler/default/Yarn%20Audit"
    },
    "ZAP": {
        "Push script": "GET /user/tools/generic/configurations/filters/ZAP/?toolType=PUSH",
        "Scan upload": "GET /api/scan-filters?tool=ZAP&triggerby=UI_UPLOAD",
        "Settings": "GET /user/tools/scheduler/default/ZAP"
    },
    "ArmorCode API": "GET /user/apikey",
    "Secure Code Warrior": "GET /api/tenant-config?configType=SECURE_CODE_WARRIOR_TRAINING_CONFIG",
    "AWS": "GET /api/awsInfra/accounts",
    "GitHub": "GET /user/tools/git/gitInstallation/repoType/GITHUB",
    "Jenkins": "GET /api/builds/?buildTool=JENKINS&sort=createdAt%2Cdesc&page=0&size=10",
    "Bamboo": "GET /api/builds/?buildTool=BAMBOO&sort=createdAt%2Cdesc&page=0&size=10",
    "Circle CI": "GET /api/builds/?buildTool=CIRCLE_CI&sort=createdAt%2Cdesc&page=0&size=10",
    "BuildKite": "GET /api/builds/?buildTool=BUILDKITE&sort=createdAt%2Cdesc&page=0&size=10",
    "Team City": "GET /api/builds/?buildTool=TEAM_CITY&sort=createdAt%2Cdesc&page=0&size=10",
    "Drone": "GET /api/builds/?buildTool=DRONE&sort=createdAt%2Cdesc&page=0&size=10",
    "Release IQ": "GET /api/builds/?buildTool=RELEASE_IQ&sort=createdAt%2Cdesc&page=0&size=10",
    "Azure Pipeline": "GET /api/builds/?buildTool=AZURE_PIPELINE&sort=createdAt%2Cdesc&page=0&size=10",
    "GitHub Actions": "GET /api/builds/?buildTool=GITHUB_ACTIONS&sort=createdAt%2Cdesc&page=0&size=10",
    "GitLab CI": "GET /api/builds/?buildTool=GITLAB_CI&sort=createdAt%2Cdesc&page=0&size=10",
    "GitLab": "GET /user/tools/git/gitInstallation/repoType/GITLAB",
    "Bitbucket": "GET /user/tools/git/gitInstallation/repoType/BITBUCKET",
    "Azure Repos": "GET /user/tools/git/gitInstallation/repoType/AZURE_REPOS",
    "Jira": "GET /user/tickets/jira/configuration/login/JIRA",
    "Azure Board": "GET /user/tickets/jira/configuration/login/AZURE_BOARD",
    "Service Now": "GET /user/tickets/jira/configuration/login/SERVICE_NOW",
    "FreshService": "GET /user/tickets/jira/configuration/login/FRESHSERVICE",
    "PagerDuty": "GET /user/tickets/jira/configuration/login/PAGERDUTY",
    "Slack": "GET /user/tools/slack/workspace?scope=BUSINESS_UNIT",
    "MS Teams": "GET /user/tools/msteams/list?scope=BUSINESS_UNIT",
    "Imperva": "GET /api/imperva",
    "Email": {},
    "ArmorCode Agent": "GET /api/ac-agent/config/all",
    "Shortcut": "GET /user/tickets/jira/configuration/login/SHORTCUT",
    "GitLab Issues": "GET /user/tickets/jira/configuration/login/GITLAB_ISSUES",
    "Automox": "GET /api/tools/automox/",
    "Rally": "GET /user/tickets/jira/configuration/login/RALLY",
    "Axonius": "GET /user/tools/generic/login_details/AXONIUS",
    "AlertConnect": {},
    "Digital.ai Agility": {},
    "ThreatConnect": "GET /user/generic/configs/THREAT_CONNECT",
    "Device42": "GET /user/tools/generic/login_details/DEVICE42",
    "Flashpoint VulnDB": {},
    "LeanIX": "GET /user/tickets/jira/configuration/login/LEAN_IX",
    "Checkmarx Codebashing": "GET /api/tenant-config?configType=CHECKMARX_CODEBASHING_TRAINING_CONFIG"
}

# Overrides

tool_map["Email"] = "???"
tool_map["AlertConnect"] = "GET /user/api/integration"
tool_map["Digital.ai Agility"] = "GET /user/tickets/jira/configuration/login/VERSION_ONE" # "GET /user/tickets/jira/configuration?0=VERSION_ONE"
tool_map["Flashpoint VulnDB"] = "GET /user/generic/configs/FLASH_POINT"
