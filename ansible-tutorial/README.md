# ansible-tutorial

Пример работы с Ansible и Vagrant

## Требования

- VirtualBox
- Vagrant
- Ansible версии 2.9.7

## Запуск вместе с Vagrant

```
vagrant box add ubuntu/xenial64
vagrant up
```

## Запуск только плейбука (требует дополнительных настроек - хоста для выполнения)

```
ansible-playbook vagrant.yml
```