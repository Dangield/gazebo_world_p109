#!/usr/bin/env python3

from shutil import copyfile
from os import mkdir, listdir, path, remove

dae_dir = '../blender_ws/exported_dae/'
models_dir = '../models/'

if __name__ == '__main__':
  for model in listdir(dae_dir):
    print(model)
    if model[-4:] == '.dae':
      model_name = model[:-4]
      model_dir = models_dir + model_name + '/'
      mesh_dir = model_dir + '/meshes/'
      config_file = model_dir + 'model.config'
      sdf_file = model_dir + 'model.sdf'

      if not path.isdir(model_dir):
        mkdir(model_dir)
      if not path.isdir(mesh_dir):
        mkdir(mesh_dir)
      copyfile(dae_dir + model, mesh_dir + 'model.dae')

      in_file = open(dae_dir + model, 'r')
      out_file = open(mesh_dir + 'model.dae', 'w')
      for line in in_file:
        out_file.write(line)
        if '<color sid="diffuse">' in line:
          color = line.split('>')[1].split('<')[0]
        if '</diffuse>' in line:
          out_file.write('            <ambient>\n')
          out_file.write('              <color sid="ambient">' + color + '</color>\n')
          out_file.write('            </ambient>\n')


      if path.exists(config_file):
        remove(config_file)
      f = open(config_file, 'w')
      f.write('<?xml version="1.0"?>' + '\n')
      f.write('<model>' + '\n')
      f.write('  <name>' + model_name + '</name>' + '\n')
      f.write('  <version>1.0</version>' + '\n')
      f.write('  <sdf version="1.0">model.sdf</sdf>' + '\n')
      f.write('  <description>' + '\n')
      f.write('    ' + model_name + '\n')
      f.write('  </description>' + '\n')
      f.write('</model>' + '\n')

      if path.exists(sdf_file):
        remove(sdf_file)
      f = open(sdf_file, 'w')
      f.write('<?xml version="1.0" ?>' + '\n')
      f.write('<sdf version="1.5">' + '\n')
      f.write('  <model name="' + model_name + '">' + '\n')
      f.write('    <static>true</static>' + '\n')
      f.write('    <link name="' + model_name + '">' + '\n')
      f.write('      <collision name="' + model_name + '">' + '\n')
      f.write('        <pose>0 0 0 0 0 0</pose>' + '\n')
      f.write('        <geometry>' + '\n')
      f.write('          <mesh>' + '\n')
      f.write('            <uri>model://' + model_name + '/meshes/model.dae</uri>' + '\n')
      f.write('          </mesh>' + '\n')
      f.write('        </geometry>' + '\n')
      f.write('      </collision>' + '\n')
      f.write('' + '\n')
      f.write('      <visual name="' + model_name + '">' + '\n')
      f.write('      <cast_shadows>true</cast_shadows>' + '\n')
      f.write('        <geometry>' + '\n')
      f.write('          <mesh>' + '\n')
      f.write('          <uri>model://' + model_name + '/meshes/model.dae</uri>' + '\n')
      f.write('        </mesh>' + '\n')
      f.write('        </geometry>' + '\n')
      f.write('      </visual>' + '\n')
      f.write('    </link>' + '\n')
      f.write('  </model>' + '\n')
      f.write('</sdf>' + '\n')