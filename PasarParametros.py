#Forma 1: modulo sys
#Se pasan los param directamente separados por espacios (comando python PasarParametros.py Param1 Param2...)
# import sys
# print("Param del script: ", sys.argv)

#Forma 2: modulo argparse
#Aqui se pueden crear argumentos mas avanzados donde cada uno reciba un nombre que los distinga, para no liarnos con cuál es el primer 
# param o el segundo (comando python PasarParametros.py --gpus=0,1,2 --batch-size=10)
import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--gpus', type=str, default = None, help='')
parser.add_argument('--batch-size', type=int, default=32)
args = parser.parse_args()
print(args.gpus)
print(args.batch_size)

#Forma 3: usando tensorflow (NO RECOMENDADO)
#Se definen ciertas FLAGS con su tipo de dato y luego en el main se ejecuta lo que queramos con el valor de esas flags 
# import tensorflow as tf
# tf.app.flags.DEFINE_string('gpus', None, 'gpus to use')
# tf.app.flags.DEFINE_integer('batch_size', 5, 'batch size')
 
# FLAGS = tf.app.flags.FLAGS
 
# def main(_):
#     print(FLAGS.gpus)
#     print(FLAGS.batch_size)
 
# if __name__=="__main__":
#     tf.app.run()