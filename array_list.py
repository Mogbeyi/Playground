tags = [
        {
          "name": "ICMP-industrycity.brk.ny"
        },
        {
          "name": "Mikrotik-v6-exporter"
        },
        {
          "name": "Mikrotik-V7"
        }
      ]

def get_names(tag_list):
    return [tag["name"] for tag in tag_list]

print(get_names(tags))
