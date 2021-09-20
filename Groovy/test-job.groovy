String tgt_job_stage='Print Var'
// String tgt_job_comment='Get SU Info for: '
String tgt_bld_job='./'

node('ec2-worker-u18-light'){
  stage(tgt_job_stage){
    String vartoprint=VAR1
    // String colleague_runtime_env=COLLEAGUE_RUNTIME_ENV
    // String aux_env_name=AUX_ENV_NAME
    // String dbtype='PGS'
    // String awsregion=AWS_REGION
    // String dnszone=DNS_ZONE

    // String search_action=SEARCH_ACTION
    // String search_mode=SEARCH_MODE
    // String search_string=SEARCH_STRING

    currentBuild.displayName = "${currentBuild.number} - ${colleague_env}/${colleague_runtime_env}/${dbtype}"
    def ARTIFACTS = colleague_env.split(',')
    //for (ARTIFACT in ARTIFACTS) {
    echo tgt_job_comment + ARTIFACT
    build job: tgt_bld_job, 
    parameters:
      [ string(name: 'VAR1', value: vartoprint),
    }
  }
}