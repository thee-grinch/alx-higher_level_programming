#!/bin/bash
#displays only body of 200 requests
curl -s -f -l $1
#!/bin/bash
# displays only body of 200 requests
curl -s -f -l $1 | grep -v "HTTP/" | sed -n '/^$/,$p'
#!/bin/bash
# displays only body of 200 requests and counts redirects
curl -s -f -l -o /dev/null -w 'with %{num_redirects} redirections' $1
