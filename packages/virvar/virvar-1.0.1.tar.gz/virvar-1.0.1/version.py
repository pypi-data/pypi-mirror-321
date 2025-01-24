# coding: utf-8
import toml
with open('pyproject.toml', 'r') as f:
    config = toml.load(f)
    
print(config['project']['version'])
version = config['project']['version'].split('.')
print(f'version={version}')
new_version = input("Enter new version name default= x.y.z where x=Major, y=Minor, z=patch/correctif?\n")
config['project']['version'] = new_version
print(f"New version={new_version}")
with open('pyproject.toml', 'w') as f:
    toml.dump(config, f)


