read -p "Enter a URL: " url
domain=$(echo $url | awk -F[/:] '{print $4}')
ping -c 4 "$domain"
