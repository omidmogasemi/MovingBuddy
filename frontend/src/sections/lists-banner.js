/** @jsx jsx */
import { jsx } from 'theme-ui';
import { Container, Box, Heading, Text, Image, Button } from 'theme-ui';

export default function ListBanner() { 
    return ( 
        <section sx={styles.banner} id="list">
             <Container sx={styles.banner.container}>
                <Box sx={styles.banner.contentBox}>
                    <Text as="h1" variant="heroSecondary">
                        Hi <span sx={{variant: "spans.primary"}}>Omid!</span> 
                    </Text>
                    <Text as="p" variant="heroThird">
                        You have currently spent <span sx={{variant: "spans.moneyCurrent"}}>$200</span> of your <span sx={{variant: "spans.moneyGoal"}}>$1000</span> goal. 
                    </Text>
                </Box> 
            </Container> 
        </section>
    )
} 

const styles = { 
    banner: { 
        pt: ['70px', '75px', '85px', '90px', null, null, '105px'],
        pb: [2, null, 0, null, 2, 0, null, 5],
        position: 'relative',
        container: {
            minHeight: 'inherit',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
        },
        contentBox: {
            width: ['100%', '90%', '535px', null, '57%', '60%', '68%', '60%'],
            mx: 'auto',
            textAlign: 'center',
            mb: ['40px', null, null, null, null, 7],
        },
    } 
}