String tgt_job_stage='Print Var'
String tgt_bld_job='./Jobs/Print-Var/'

node('ec2-worker-u18-light'){
  stage(tgt_job_stage){
    String vartoprint=VAR1
    build job: tgt_bld_job, 
    parameters:
      [ string(name: 'VAR1', value: vartoprint) ]

}