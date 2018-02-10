# SSM-Shell
Open a limited shell to an EC2 instance using the SSM Agent and SSM RunCommand. Execute commands on EC2 without maintaining SSH keys.

### Prerequisites
- An EC2 instance with SSM agent installed
- IAM credentials with permissions SSM:SendCommand and SSM:GetCommandInvocation

### Limitations
- Commands are executed in a fresh environment each time (no real shell). So you cannot do `cd /mydir` and expect a following `ls` to return the content of `/mydir`.

### Usage
`./shell i-01234567890`
