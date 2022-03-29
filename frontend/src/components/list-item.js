/** @jsx jsx */ 
import { useState} from 'react'; 
import { jsx } from 'theme-ui'; 
import { Container, Grid, Box, Text, Label, Checkbox, Image } from 'theme-ui'; 
import copy from 'assets/list-item/copy.png'; 
import edit from 'assets/list-item/edit.png'; 
import trash from 'assets/list-item/trash.png'; 

export default function ListItem() { 
    const [display, setDisplay] = useState('none'); 
    const mouseEnter = () => setDisplay('inline-block'); 
    const mouseLeave = () => setDisplay('none'); 

    return ( 
        <Container 
            onMouseEnter={mouseEnter} 
            onMouseLeave={mouseLeave}
            sx={styles.container}
        >
            <Image src={copy} sx={styles.icon}/>
            <Text sx={styles.list_title}>Television</Text>
            <Image src={copy} sx={styles.icon}/>
            <Image src={edit} sx={{...styles.icon, display: display}}/>
            <Image src={trash} sx={{...styles.icon, display: display}} />
        </Container>
    ) 
} 

const styles = { 
    list_title: { 
        width: '175px', 
        position: 'relative',
        top: '-5px', 
        display: 'inline-block',
    }, 
    icon: { 
        display: 'inline-block', 
        maxWidth: '32px', 
        minWidth: '32px', 
        pr: '10px !important',
    },     
    container: { 
        width: '370px', 
    }, 
} 