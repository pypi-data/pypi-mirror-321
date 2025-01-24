import numpy as np
from tcrsep.estimator import TCRsep
from tcrsep.dataset import *
import logging
from tcrsep.utils import *
import os
import argparse
import gzip
import json

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='') 
    parser.add_argument('--post_data_path',type=str)
    parser.add_argument('--save_dir',type=str,default='result/')
    parser.add_argument('--pre_data_path',type=str,default='None')
    parser.add_argument('--gen_model_path',type=str,default='None')
    parser.add_argument('--epochs',type=int,default=500)
    parser.add_argument('--alpha',type=float,default=0.1)
    parser.add_argument('--batchsize',type=int,default=512)    
    parser.add_argument('--val_ratio',type=float,default=0.1)  
    parser.add_argument('--lr',type=float,default=1e-4)      
    parser.add_argument('--device',type=str,default='cuda:0')
    parser.add_argument('--save_emb',action='store_true',default=False)          
    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.mkdir(args.save_dir) 
    save_model_path = os.path.join(args.save_dir,'tcrsep.pth')
    save_pre_emb_path = os.path.join(args.save_dir,'pre_emb.npy.gz')
    save_post_emb_path = os.path.join(args.save_dir,'post_emb.npy.gz')
    save_args_path = os.path.join(args.save_dir,'args.json')
    save_pre_path = os.path.join(args.save_dir,'pre-sel.csv')
    
    gen_seqs = None
    emb_pre = False
    if args.pre_data_path != "None":
        if args.pre_data_path.endswith('.npy.gz'):
            f = gzip.GzipFile(args.pre_data_path, "r")
            gen_seqs = np.load(f)
            logger.info('Done loading embeddings for pre-selection clonetypes')
            emb_pre = True
        else :
            sep = ',' if '.csv' in args.pre_data_path else '\t'
            pre_df = pd.read_csv(args.pre_data_path,sep=sep)
            if len(pre_df) > 5000000:                
                pre_df = pd.read_csv(args.pre_data_path,sep=sep,nrows=5000000)
            gen_seqs = np.array(pre_df[['CDR3.beta','V','J']])
            logger.info(f'Done loading pre-sel TCR data from {args.pre_data_path}')
    
    if args.post_data_path.endswith('.npy.gz'):
        f = gzip.GzipFile(args.post_data_path, "r")
        post_seqs = np.load(f)
        logger.info('Done loading embeddings for post-selection clonetypes')
    else:
        sep = ',' if '.csv' in args.post_data_path else '\t'
        post_seqs = pd.read_csv(args.post_data_path,sep=sep)
        if len(post_seqs) > 5000000:
            post_seqs = pd.read_csv(args.post_data_path,sep=sep,nrows=5000000)
        post_seqs = post_seqs[['CDR3.beta','V','J']].values
        logger.info(f'Done loading TCR data from {args.post_data_path}')

    sel_model = TCRsep(alpha=args.alpha,gen_model_path=args.gen_model_path,device=args.device,lr=args.lr)
    
    seqs_pre,pre_emb,post_emb = sel_model.train(args.epochs,post_seqs,gen_seqs,args.batchsize,save_model_path,args.val_ratio)

    if args.save_emb:
        f = gzip.GzipFile(save_pre_emb_path, "w") 
        np.save(file=f, arr=pre_emb)

        f = gzip.GzipFile(save_post_emb_path, "w") 
        np.save(file=f, arr=post_emb)

    with open(save_args_path,'wt') as f:
        args.Z = str(sel_model.Z)
        json.dump(vars(args),f,indent=4)        

    if gen_seqs is None and not emb_pre:
        logger.info("Saving the generated pre-selection samples.")
        pre_df = pd.DataFrame({'CDR3.beta':[s[0] for s in seqs_pre],'V':[s[1] for s in seqs_pre],'J':[s[2] for s in seqs_pre]})
        pre_df.to_csv(save_pre_path,index=False)    